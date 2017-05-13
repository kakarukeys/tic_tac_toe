#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tic_tac_toe.ai as ai


def test_node_children():
    node = ai.Node('O', 5, ['X', 2, 'O', 4, 'O', 'X', 'O', 'X'])

    children = list(node.children)

    assert len(children) == 2

    assert children[0].marker == 'X'
    assert children[0].move == 2
    assert children[0].game_state == ['X', 'X', 'O', 4, 'O', 'X', 'O', 'X']

    assert children[1].marker == 'X'
    assert children[1].move == 4
    assert children[1].game_state == ['X', 2, 'O', 'X', 'O', 'X', 'O', 'X']


def test_is_terminal():
    assert not ai.is_terminal(ai.Node('O', 5, ['X', 2, 'O', 4, 'O', 'X', 7, 'X', 'O']))
    assert ai.is_terminal(ai.Node('O', 5, ['X', 'X', 'O', 'O', 'O', 'X', 'O', 'X', 'X']))
    assert ai.is_terminal(ai.Node('X', 6, ['X', 'O', 3, 'X', 'X', 'X', 'O', 8, 'O']))


def test_evaluate():
    assert ai.evaluate(ai.Node('X', 9, ['X', 'O', 'O', 'O', 'X', 6, 'X', 8, 'X'])) == 1
    assert ai.evaluate(ai.Node('O', 3, ['X', 'O', 'O', 'O', 'X', 6, 'X', 8, 9])) == 0
    assert ai.evaluate(ai.Node('O', 9, ['O', 'X', 'X', 'X', 'O', 6, 7, 8, 'O'])) == -1


def test_minimax():
    # O's turn, O mates in 1 move
    node = ai.Node('X', 4, ['O', 'X', 'X', 'X', 'O', 6, 7, 8, 9])
    assert ai.minimax(node, depth=0, maximize=False) == 0
    assert ai.minimax(node, depth=1, maximize=False) == -1
    assert ai.minimax(node, depth=2, maximize=False) == -1

    # O's turn, X mates in 1 move
    node = ai.Node('X', 5, ['X', 'O', 3, 'X', 'X', 6, 'O', 8, 9])
    assert ai.minimax(node, depth=0, maximize=False) == 0
    assert ai.minimax(node, depth=1, maximize=False) == 0
    assert ai.minimax(node, depth=2, maximize=False) == 1
    assert ai.minimax(node, depth=3, maximize=False) == 1

    # X's turn, X mates in 2 moves
    node = ai.Node('O', 7, ['X', 'O', 3, 'X', 5, 6, 'O', 8, 9])
    assert ai.minimax(node, depth=0, maximize=True) == 0
    assert ai.minimax(node, depth=1, maximize=True) == 0
    assert ai.minimax(node, depth=2, maximize=True) == 0
    assert ai.minimax(node, depth=3, maximize=True) == 1
    assert ai.minimax(node, depth=4, maximize=True) == 1

    # end game
    node = ai.Node('X', 9, ['O', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'X'])
    assert ai.minimax(node, depth=1, maximize=False) == 0
