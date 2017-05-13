from typing import NamedTuple, Iterable

from .game import GameState
from . import game


OPPONENT_MARKER = dict(zip(game.MARKERS, reversed(game.MARKERS)))

WINNING_SCORE = {'X': 1, 'O': -1}

BaseNode = NamedTuple("BaseNode", [
    ("marker", str),
    ("move", int),

    # as a result of marker and move
    ("game_state", GameState)
])


class Node(BaseNode):
    @property
    def children(self) -> Iterable[BaseNode]:
        """ yield all possible nodes of next move """
        next_marker = OPPONENT_MARKER[self.marker]

        for move in game.gen_available_moves(self.game_state):
            new_game_state = game.play_move(self.game_state, next_marker, move)
            yield Node(next_marker, move, new_game_state)


def is_terminal(node: Node) -> bool:
    """ return whether the node contains a won or drawn game """
    return game.is_finished(node.game_state) or \
        game.is_winning_move(node.game_state, node.marker, node.move)


def evaluate(node: Node) -> int:
    """ return a score to indicate how favorable the game is to player holding
        marker X
    """
    if game.is_winning_move(node.game_state, node.marker, node.move):
        return WINNING_SCORE[node.marker]
    else:
        return 0


def minimax(node: Node, depth: int, maximize: bool) -> int:
    """ Minimax algorithm, refer to
        https://en.wikipedia.org/wiki/Minimax#Pseudocode
    """
    if depth == 0 or is_terminal(node):
        return evaluate(node)

    select = max if maximize else min

    return select(
        minimax(child, depth - 1, not maximize)
        for child in node.children
    )


def compute_next_move(next_marker: str, game_state: GameState) -> Node:
    """ return the most optimal move to place <next_marker> in <game_state> """
    last_marker = OPPONENT_MARKER[next_marker]
    node = Node(last_marker, None, game_state)

    select = max if next_marker == 'X' else min

    return select(
        node.children,
        key=lambda n: minimax(n, depth=5, maximize=next_marker != 'X')
    )
