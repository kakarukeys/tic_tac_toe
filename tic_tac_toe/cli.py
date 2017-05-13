# -*- coding: utf-8 -*-

from itertools import cycle

import click

from . import game, board, ai


def ask_for_player_name(player_number):
    return click.prompt(
        "Player {}, how may I address you".format(player_number),
        prompt_suffix='? '
    )


def ask_for_player_move(player_name, game_state):
    while True:
        move = click.prompt(
            "{}, it's your turn! Your move".format(player_name),
            type=int,
            prompt_suffix='? '
        )

        if game.is_valid_move(game_state, move):
            return move

        click.echo("Please enter a valid move.")


@click.command()
def main(args=None):
    click.echo("Tic Tac Toe - two players")

    # on-board players
    players = []

    for i in range(2):
        players.append(ask_for_player_name(i + 1))

    click.echo("\n{0} vs {1}\n".format(*players))

    # initialize the game
    assigned_markers = dict(zip(players, game.MARKERS))
    game_state = game.create_initial_state()

    # print the empty board
    click.echo(board.render(game_state))

    # play the game till won or drawn
    for active_player in cycle(players):
        marker = assigned_markers[active_player]

        if active_player.lower() == "computer":
            click.echo("computer thinking...")
            result = ai.compute_next_move(marker, game_state)
            move = result.move
            game_state = result.game_state
        else:
            move = ask_for_player_move(active_player, game_state)
            game_state = game.play_move(game_state, marker, move)

        click.echo(move)
        click.echo(board.render(game_state))

        if game.is_winning_move(game_state, marker, move):
            click.echo("{} has won the game!".format(active_player))
            break
        elif game.is_finished(game_state):
            click.echo("The game is drawn.")
            break


if __name__ == "__main__":
    main()
