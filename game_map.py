from __future__ import annotations

from typing import Iterable, Iterator, Optional, TYPE_CHECKING

import numpy as np  # type: ignore
import tcod.los
from tcod.console import Console

import tile_types
from colours_and_chars import MapColoursChars
from entity import Actor, Item
from random import choice
import colour
from player_generator import generate_player, add_player

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity

new_player_chance = (True, False, False, False, False, False, False, False, False, False, False, False, False, False,
                     False, False, False, False, False, False, False, False, False, False, False)


def _get_view_slice(screen_width: int, world_width: int, anchor: int):
    """Return 1D (screen_view, world_view) slices.

    Letterboxing is added to fit the views to the screen.
    Out-of-bounds slices are zero width and will result in zero length arrays when used.

    Args:
        screen_width: The width of the screen shape.
        world_width: The width of the world shape.
        anchor: The world point to place at screen position zero.
    """
    # Moving the anchor past the left of the world will push the screen to the right.
    # This adds the leftmost letterbox to the screen.
    screen_left = max(0, -anchor)
    # The anchor moving past the left of the world will slice into the world from the left.
    # This keeps the world view in sync with the screen and the leftmost letterbox.
    world_left = max(0, anchor)
    # The view width is clamped to the smallest possible size between the screen and world.
    # This adds the rightmost letterbox to the screen.
    # The screen and world can be out-of-bounds of each other, causing a width of zero.
    view_width = max(0, min(screen_width - screen_left, world_width - world_left))
    screen_view = slice(screen_left, screen_left + view_width)
    world_view = slice(world_left, world_left + view_width)
    return screen_view, world_view


def get_views(screen_shape, world_shape, anchor):
    """Return (screen_view, world_view) as 2D slices for use with NumPy.

    These views are used to slice their respective arrays.
    `anchor` should be (i, j) or (x, y) depending on the order of the shapes.
    Letterboxing is added to the views to make them fit.
    Out-of-bounds views are zero width.

    Args:
        screen_shape: The shape of the screen array.
        world_shape: The shape of the world array.
        anchor: The world point to place at (0, 0) on the screen.

    Example::

        camera: tuple[int, int]  # (y, x) by default, (x, y) if arrays are order="F".
        screen: NDArray[Any]
        world: NDArray[Any]
        screen_view, world_view = get_views(camera, screen.shape, world.shape)
        screen[screen_view] = world[world_view]
    """
    i_slice = _get_view_slice(screen_shape[0], world_shape[0], anchor[0])
    j_slice = _get_view_slice(screen_shape[1], world_shape[1], anchor[1])
    return (i_slice[0], j_slice[0]), (i_slice[1], j_slice[1])


class GameMap:
    def __init__(self, engine: Engine, width: int, height: int,
                 entities: Iterable[Entity] = (), fov_radius: int = 15):
        self.engine = engine
        self.fov_radius = fov_radius

        self.colours_chars = MapColoursChars(self.engine.current_level)

        # defines the colours and characters used for wall tiles:
        self.wall = tile_types.new_wall(self.colours_chars.wall_fg_dark,
                                        self.colours_chars.wall_bg_dark,
                                        self.colours_chars.wall_fg_light,
                                        self.colours_chars.wall_bg_light,
                                        self.colours_chars.wall_tile)

        self.entities = set(entities)
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=self.wall, order="F")  # fills game map with wall tiles

        self.zeros = np.zeros((width, height), dtype=bool)

        self.visible = np.full(
            (width, height), fill_value=False, order="F"
        )  # Tiles the player can currently see

        for player in self.engine.players:
            player.fighter.visible_tiles = np.full(
                (width, height), fill_value=False, order="F"
            )

        self.explored = np.full(
            (width, height), fill_value=False, order="F"
        )  # Tiles the player has seen before

        self.downstairs_location = (0, 0)

        self.rooms = []

        self.camera_xy = (0, 0)  # Camera center position.

    @property
    def gamemap(self) -> GameMap:
        return self

    @property
    def actors(self) -> Iterator[Actor]:
        """Iterate over this maps living actors."""
        yield from (
            entity
            for entity in self.entities
            if isinstance(entity, Actor) and entity.is_alive
        )

    @property
    def items(self) -> Iterator[Item]:
        yield from (entity for entity in self.entities if isinstance(entity, Item))

    def get_blocking_entity_at_location(
            self, location_x: int, location_y: int,
    ) -> Optional[Entity]:
        for entity in self.entities:
            if (
                    entity.blocks_movement
                    and entity.x == location_x
                    and entity.y == location_y
            ):
                return entity

        return None

    def get_actor_at_location(self, x: int, y: int) -> Optional[Actor]:
        for actor in self.actors:
            if actor.x == x and actor.y == y:
                return actor

        return None

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def get_left_top_pos(self, screen_shape):
        """Return the (left, top) position of the camera for a screen of this size."""
        return self.camera_xy[0] - screen_shape[0] // 2, self.camera_xy[1] - screen_shape[1] // 2

    def render(self, console: Console) -> None:

        screen_shape = console.rgb.shape
        cam_x, cam_y = self.get_left_top_pos(screen_shape)

        # Get the screen and world view slices.
        screen_view, world_view = get_views(screen_shape, self.tiles.shape, (cam_x, cam_y))

        # Draw the console based on visible or explored areas.
        console.tiles_rgb[screen_view] = np.select(
            (self.visible[world_view], self.explored[world_view]),
            (self.tiles["light"][world_view], self.tiles["dark"][world_view]),
            tile_types.SHROUD,
        )

        entities_sorted_for_rendering = sorted(
            self.entities, key=lambda x: x.render_order.value
        )

        for entity in entities_sorted_for_rendering:

            # entity is visible
            if self.visible[entity.x, entity.y]:
                entity.seen = True
                # sets 'ghost position' at last seen location
                entity.ghost_x = entity.x
                entity.ghost_y = entity.y
                obj_x, obj_y = entity.x - cam_x, entity.y - cam_y
                # prints entity to console
                if 0 <= obj_x < console.width and 0 <= obj_y < console.height:
                    # non-player characters that cannot be seen directly by the player character currently being
                    # controlled by the player are printed in grey to indicate that they cannot be attacked
                    if isinstance(entity, Actor) and entity not in self.engine.players:
                        if self.engine.player.fighter.visible_tiles[entity.x, entity.y]:
                            console.tiles_rgb[["ch", "fg"]][obj_x, obj_y] = ord(entity.char), entity.fg_colour
                        else:
                            console.tiles_rgb[["ch", "fg"]][obj_x, obj_y] = ord(entity.char), colour.LIGHT_GRAY
                    else:
                        console.tiles_rgb[["ch", "fg"]][obj_x, obj_y] = ord(entity.char), entity.fg_colour

            # entity has been seen before
            elif entity.seen:

                # if ghost position visible, sets seen to false
                if self.visible[entity.ghost_x, entity.ghost_y]:
                    entity.seen = False
                # ghost position not visible, prints ghost to console
                else:
                    obj_x, obj_y = entity.ghost_x - cam_x, entity.ghost_y - cam_y
                    if 0 <= obj_x < console.width and 0 <= obj_y < console.height:
                        console.tiles_rgb[["ch", "fg"]][obj_x, obj_y] = ord(entity.char), colour.LIGHT_GRAY

    def check_los(self, start_x: int, start_y: int, end_x: int, end_y: int):
        # checks if line of sight exists between two positions
        los = tcod.los.bresenham((start_x, start_y), (end_x, end_y)).tolist()
        for tile in los:
            # checks if tile is walkable
            if not self.tiles[tile[0], tile[1]][0]:
                return False

        return True

    def move_camera(self, x: int, y: int) -> None:

        # moves the camera if within bounds of the map
        camera_xy_updated = (self.camera_xy[0] + x, self.camera_xy[1] + y)
        if 0 <= camera_xy_updated[0] < self.width and 0 <= camera_xy_updated[1] < self.height:
            self.camera_xy = camera_xy_updated

    def generate_level(self) -> None:
        from level_generator import MessyBSPTree
        from level_parameters import level_params

        new_player = False

        self.engine.current_floor += 1

        if len(self.engine.players) < 5:
            # TODO - extend for other floors
            if self.engine.current_level == 0:
                if self.engine.current_floor == 2:
                    new_player = generate_player(current_level=self.engine.current_level, players=self.engine.players)
                    add_player(engine=self.engine, player=new_player)
                if self.engine.current_floor == 5:
                    self.engine.current_level += 1
                    self.engine.current_floor = 0

                if not new_player:
                    if choice(new_player_chance):
                        generate_player(current_level=self.engine.current_level, players=self.engine.players)
                        add_player(engine=self.engine, player=new_player)

        self.engine.game_map = MessyBSPTree(
            messy_tunnels=level_params[self.engine.current_level][0],
            map_width=level_params[self.engine.current_level][1],
            map_height=level_params[self.engine.current_level][2],
            max_leaf_size=level_params[self.engine.current_level][3],
            room_max_size=level_params[self.engine.current_level][4],
            room_min_size=level_params[self.engine.current_level][5],
            max_items_per_room=level_params[self.engine.current_level][6],
            engine=self.engine,
            current_level=self.engine.current_level,
            fov_radius=level_params[self.engine.current_level][7]
        ).generate_level()
