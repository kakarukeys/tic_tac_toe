# -*- coding: utf-8 -*-

BOARD_TEMPLATE = """
 {0} | {1} | {2}
---+---+---
 {3} | {4} | {5}
---+---+---
 {6} | {7} | {8}
"""


def render(game_state):
    """ return the game board in a string """
    return BOARD_TEMPLATE.format(*game_state)
