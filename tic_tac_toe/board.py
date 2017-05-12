# -*- coding: utf-8 -*-

from .game import GameState


BOARD_TEMPLATE = """
 {0} | {1} | {2}
---+---+---
 {3} | {4} | {5}
---+---+---
 {6} | {7} | {8}
"""


def render(game_state: GameState) -> str:
    """ return the game board in a string """
    return BOARD_TEMPLATE.format(*game_state)
