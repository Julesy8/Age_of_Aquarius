"""Handle the loading and initialization of game sessions."""
from __future__ import annotations

from typing import Optional

import tcod
import numpy as np
import lzma
import pickle
import traceback

import colour
from engine import Engine
import input_handlers
from entity import Actor
from level_generator import MessyBSPTree
from level_parameters import level_params
from components.inventory import Inventory
from components.ai import BaseAI
from components.npc_templates import Fighter
from components.bodyparts import Body, Arm, Leg, Head

from copy import deepcopy

from components.weapons.glock17 import glock_17

#from components.weapons.glock17 import glock17_frame, glock17_barrel, glock17l_barrel, \
#    glock17_barrel_ported, glock17l_barrel_ported, glock17_slide, glock17l_slide, glock17_slide_custom, \
#    glock17l_slide_custom, glock_switch, glock_9mm_compensator, \
#    glock_stock, glock_pic_rail, glock_pistol_brace

#from components.weapons.mosin import mosin_stock, mosin_archangel_stock, mosin_carbine_stock, mosin_obrez_stock, \
#    mosin_barrel, mosin_carbine_barrel, mosin_obrez_barrel, mosin_pic_scope_mount, \
#    mosin_magazine_conversion, mosin_suppressor, mosin_muzzlebreak, mosin_nagant


def new_game() -> Engine:
    """Return a brand new game session as an Engine instance."""
    current_level = 0

    # initialises player entity
    fighter_component = Fighter(unarmed_meat_damage=10, unarmed_armour_damage=5)

    #TODO: adjust to be correct
    Head_part = Head(hp=50, defence=50, depth=15, width=15, height=20)
    Body_part = Body(hp=100, defence=50, depth=20, width=15, height=20)
    R_Arm = Arm(hp=30, defence=50, name='right arm', depth=15, width=15, height=20)
    L_Arm = Arm(hp=30, defence=50, name='left arm', depth=15, width=15, height=20)
    R_Leg = Leg(hp=30, defence=50, name='right leg', depth=15, width=15, height=20)
    L_Leg = Leg(hp=30, defence=50, name='left leg', depth=15, width=15, height=20)

    body_parts = (Body_part, Head_part, R_Arm, L_Arm, R_Leg, L_Leg)

    player = Actor(0,
                   0,
                   '@',
                   colour.GREEN,
                   'Player',
                   ai=BaseAI,
                   fighter=fighter_component,
                   bodyparts=body_parts,
                   player=True,
                   inventory=Inventory(capacity=15),
                   )

    engine = Engine(player=player, current_level=current_level, current_floor=0)

    inventory_items = []

    #inventory_items = [mac1045,]

    inventory_items = [glock_17]

    #inventory_items = [glock17_frame, glock17_barrel, glock17l_barrel,
    #                   glock17_barrel_ported, glock17l_barrel_ported, glock17_slide, glock17l_slide,
    #                   glock17_slide_custom, glock17l_slide_custom,
    #                   glock_switch, glock_9mm_compensator, glock_stock, glock_pic_rail, glock_pistol_brace]

    #inventory_items = [mosin_stock, mosin_archangel_stock, mosin_carbine_stock, mosin_obrez_stock,
    #                   mosin_barrel, mosin_carbine_barrel, mosin_obrez_barrel, mosin_pic_scope_mount,
    #                   mosin_magazine_conversion, mosin_suppressor, mosin_muzzlebreak]

    #inventory_items = [mac1045_lower, mac1045_upper, mac1045_upper_tactical, mac1045_upper_max,mac1045_barrel,
    #                   mac1045_extended_barrel, mac1045_carbine_barrel, mac10_full_stock, mac10_folding_stock,
    #                   mac1045_sionics_suppressor, mac109_max_barrel, mac1045_max_barrel, mac10_vertical_grip]

    for item in inventory_items:
        itemcopy = deepcopy(item)
        player.inventory.items.append(itemcopy)
        itemcopy.parent = player.inventory

    engine.game_map = MessyBSPTree(level_params[current_level][0],  # messy tunnels
                                   level_params[current_level][1],  # map width
                                   level_params[current_level][2],  # map height
                                   level_params[current_level][3],  # max leaf size
                                   level_params[current_level][4],  # max room size
                                   level_params[current_level][5],  # room min size
                                   level_params[current_level][6],  # max monsters per room
                                   level_params[current_level][7],  # max items per room
                                   engine,
                                   current_level,
                                   ).generateLevel()

    engine.game_map.camera_xy = (engine.player.x, engine.player.y)

    engine.update_fov()

    engine.message_log.add_message(
        "You lose your footing and fall deep into the caverns below... You can't see any way to get back to the surface"
        , colour.LIGHT_MAGENTA
    )

    return engine


def load_game(filename: str) -> Engine:
    """Load an Engine instance from a file."""
    with open(filename, "rb") as f:
        engine = pickle.loads(lzma.decompress(f.read()))
    assert isinstance(engine, Engine)
    return engine


class MainMenu(input_handlers.BaseEventHandler):
    """Handle the main menu rendering and input."""

    def __init__(self):
        self.option_selected = 0

    def on_render(self, console: tcod.Console) -> None:
        """Render the main menu on a background image."""

        path = "newmenu1.xp"  # REXPaint file with one layer.
        # Load a REXPaint file with a single layer.
        # The comma after console is used to unpack a single item tuple.
        console2, = tcod.console.load_xp(path, order="F")

        # Convert tcod's Code Page 437 character mapping into a NumPy array.
        CP437_TO_UNICODE = np.asarray(tcod.tileset.CHARMAP_CP437)

        # Convert from REXPaint's CP437 encoding to Unicode in-place.
        console2.ch[:] = CP437_TO_UNICODE[console2.ch]

        # Apply REXPaint's alpha key color.
        KEY_COLOR = (255, 0, 255)
        is_transparent = (console2.rgb["bg"] == KEY_COLOR).all(axis=2)
        console2.rgba[is_transparent] = (ord(" "), (0,), (0,))

        console2.blit(dest=console, dest_x=console.width//2-17, dest_y=console.height//2-17, src_x=0, src_y=0, width=35, height=35)

        console.print(
            console.width // 2,
            console.height - 2,
            "Submit bug reports and suggestions to DeepUndergroundRL@protonmail.com",
            fg=colour.WHITE,
            alignment=tcod.CENTER,
        )
        console.print(
            1,
            1,
            "Pre-alpha",
            fg=colour.WHITE,
        )

        menu_width = 8
        for i, text in enumerate(
            ["New Game", "Continue", "Quit"]
        ):
            console.print(
                console.width // 2,
                console.height // 2 - 2 + i,
                text.ljust(menu_width),
                fg=colour.RED,
                alignment=tcod.CENTER,
                bg_blend=tcod.BKGND_ALPHA(64),
            )

        console.print(x=console.width // 2 - 5, y=console.height // 2 - 2 + self.option_selected, string='>', fg=colour.WHITE)

    def ev_keydown(
        self, event: tcod.event.KeyDown
    ) -> Optional[input_handlers.BaseEventHandler]:
        if event.sym == tcod.event.K_ESCAPE:
            raise SystemExit()

        elif event.sym == tcod.event.K_DOWN:
            if self.option_selected < 2:
                self.option_selected += 1

        elif event.sym == tcod.event.K_UP:
            if self.option_selected > 0:
                self.option_selected -= 1

        elif event.sym == tcod.event.K_RETURN:
            if self.option_selected == 0:
                return input_handlers.MainGameEventHandler(new_game())
            elif self.option_selected == 1:
                try:
                    return input_handlers.MainGameEventHandler(load_game("savegame.sav"))
                except FileNotFoundError:
                    return input_handlers.PopupMessage(self, "No saved game to load.")
                except Exception as exc:
                    traceback.print_exc()  # Print to stderr.
                    return input_handlers.PopupMessage(self, f"Failed to load save:\n{exc}")
                pass
            elif self.option_selected == 2:
                raise SystemExit()

        return None
