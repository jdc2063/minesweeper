import random

import pytest

from src.minesweeper import Minesweeper


def test_module_exists():
    import src.minesweeper as minesweeper

    assert minesweeper


# Define a fixture for the Minesweeper game instance
@pytest.fixture
def game():
    # Create a new Minesweeper game with a 5x5 grid and 3 mines
    return Minesweeper(5, 5, 3)


def test_board_initialization(game):
    # Ensure the game board is correctly initialized
    assert game.rows == 5
    assert game.cols == 5
    assert game.num_mines == 3
    assert len(game.board) == 5
    assert len(game.board[0]) == 5
    assert len(game.mines) == 3


def test_mine_placement(game):
    # Ensure that mines are placed correctly on the board
    mine_count = sum(row.count("💣") for row in game.board)
    assert mine_count == 3


def test_reveal_cell(game):
    # Assume the cell at (2, 2) is surrounded by no mines

    random.seed(0)
    game.board[2][2] = "0"
    game.reveal(2, 2)
    print(game.revealed)
    # Ensure the cell is revealed
    assert (2, 2) in game.revealed


def test_game_over(game):
    # Force a mine at a specific location
    game.mines = {(1, 1)}
    game.board[1][1] = "M"

    # Reveal the mine and check if the game ends
    result = game.reveal(1, 1)
    assert result == "Game Over"


def test_win_condition(game):
    # Simulate all cells except mines being revealed
    game.revealed = set(
        (r, c) for r in range(5) for c in range(5) if (r, c) not in game.mines
    )

    # Ensure the game recognizes a win condition
    assert game.is_winner() is True
