# -*- coding: utf-8 -*-

from typing import List, Union


"""
    Game state consists of markers and valid moves
    e.g. ['X', 2, 'O', 4, 5, 6, 7, 8, 9, 10]
"""

GameState = List[Union[int, str]]

INITIAL_STATE = tuple(range(1, 10))

MARKERS = ('X', 'O')

ADJACENT_POSITIONS = (
    # rows
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),

    # columns
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),

    # diagonals
    (0, 4, 8),
    (6, 4, 2),
)


def create_initial_state() -> GameState:
    """ return the game state that represents the start of a new game """
    return list(INITIAL_STATE)


def is_valid_move(game_state: GameState, move: int) -> bool:
    """ return whether <move> is valid on <game_state> """
    return move in game_state


def is_winning_move(game_state: GameState, marker: str, move: int) -> bool:
    """ return whether the <move> wins the game with <marker> in
        <game_state>
    """
    move_pos = move - 1

    # the test should work regardless of whether game_state is before or
    # after the move is played
    return any(
        all(game_state[pos] == marker for pos in triplet if pos != move_pos)
        for triplet in ADJACENT_POSITIONS
        if move_pos in triplet
    )


def play_move(game_state: GameState, marker: str, move: int) -> GameState:
    """ return new game state after <move> is played with <marker> on
        <game_state>
    """
    move_pos = move - 1

    new_game_state = list(game_state)
    new_game_state[move_pos] = marker
    return new_game_state


def is_finished(game_state: GameState) -> bool:
    """ return whether the game is fully played out """
    return all(isinstance(x, str) for x in game_state)
