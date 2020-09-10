from typing import Tuple

import numpy as np  # type: ignore

# Tile graphics structured type compatible with Console.tiles_rgb.
graphic_dt = np.dtype(
    [
        ("ch", np.int32),  # Unicode codepoint.
        ("fg", "3B"),  # 3 unsigned bytes, for RGB colors.
        ("bg", "3B"),
    ]
)

# Tile struct used for statically defined tile data.
tile_dt = np.dtype(
    [
        ("walkable", np.bool),  # True if this tile can be walked over.
        ("transparent", np.bool),  # True if this tile doesn't block FOV.
        ("dark", graphic_dt),  # Graphics for when this tile is not in FOV.
    ]
)


def new_tile(
    *,  # Enforce the use of keywords, so that parameter order doesn't matter.
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper function for defining individual tile types """
    return np.array((walkable, transparent, dark), dtype=tile_dt)


def new_floor(bg_colour: Tuple[int, int, int], fg_colour: Tuple[int, int, int], tile: int):
    floor = new_tile(
        walkable=True, transparent=True, dark=(tile, fg_colour, bg_colour),
    )
    return floor


def new_wall(bg_colour, fg_colour, tile):
    wall = new_tile(
        walkable=False, transparent=False, dark=(tile, fg_colour, bg_colour),
    )
    return wall
