#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tic_tac_toe.game as game


def test_create_initial_state():
    assert game.create_initial_state() == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert game.create_initial_state() is not game.create_initial_state()


def test_is_valid_move():
    assert game.is_valid_move(['X', 2, 3, 4, 5, 6, 7, 8, 9], 2)
    assert not game.is_valid_move(['X', 2, 3, 4, 5, 6, 7, 8, 9], 1)


def test_is_winning_move():
    # rows
    assert game.is_winning_move(['X', 'X', 'X', 4, 5, 6, 7, 8, 9], 'X', 3)
    assert game.is_winning_move([1, 2, 3, 'X', 'X', 'X', 7, 8, 9], 'X', 6)
    assert game.is_winning_move([1, 2, 3, 4, 5, 6, 'X', 'X', 'X'], 'X', 9)

    # the move has not been played
    assert game.is_winning_move([1, 2, 3, 4, 5, 6, 'X', 'X', 9], 'X', 9)

    # wrong marker arg
    assert not game.is_winning_move([1, 2, 3, 4, 5, 6, 'X', 'X', 'X'], 'O', 9)

    # wrong move arg
    assert not game.is_winning_move([1, 2, 3, 4, 5, 6, 'X', 'X', 'X'], 'X', 1)

    # columns
    assert game.is_winning_move(['O', 2, 3, 'O', 5, 6, 'O', 8, 9], 'O', 7)
    assert game.is_winning_move([1, 'O', 3, 4, 'O', 6, 7, 'O', 9], 'O', 8)
    assert game.is_winning_move([1, 2, 'O', 4, 5, 'O', 7, 8, 'O'], 'O', 9)

    # diagonals
    assert game.is_winning_move(['X', 2, 3, 4, 'X', 6, 7, 8, 'X'], 'X', 9)
    assert game.is_winning_move([1, 2, 'O', 4, 'O', 6, 'O', 8, 9], 'O', 3)


def test_play_move():
    old_state = ['X', 2, 3, 4, 5, 6, 7, 8, 9]

    new_state = game.play_move(old_state, 'O', 2)

    assert new_state == ['X', 'O', 3, 4, 5, 6, 7, 8, 9]
    assert old_state is not new_state


def test_is_finished():
    assert game.is_finished(['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O'])

    assert not game.is_finished(
        ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 9]
    )
