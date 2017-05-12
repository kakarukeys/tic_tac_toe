# -*- coding: utf-8 -*-

import click


@click.command()
def main(args=None):
    click.echo("Tic Tac Toe - two players")


if __name__ == "__main__":
    main()
