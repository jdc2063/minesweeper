import pytest
import src.minesweeper.minesweeper as minesweeper

def test_module_exists():
    assert minesweeper

def test_place_mines():
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    assert len(game.mines) == 2

def test_reveal():
    import random 
    random.seed(0)
    game = minesweeper.Minesweeper(3, 3, 2)
    game.reveal(2, 2)
    assert game.revealed == {(2, 2)}

def test_get_board():
    import random 
    random.seed(0)
    game = minesweeper.Minesweeper(3, 3, 2)
    game.reveal(2, 2)
    assert game.get_board() == [['?', '?', '?'], ['?', '?', '?'], ['?', '?', 1]]

    
def test_get_winner():
    import random 
    random.seed(0)
    game = minesweeper.Minesweeper(3, 3, 2)
    game.reveal(2, 2)
    assert game.is_winner() == False

def test_restart():
    import random 
    random.seed(0)
    game = minesweeper.Minesweeper(3, 3, 2)
    old_mine = game.mines
    random.seed(1)
    game.restart()
    assert game.mines != old_mine
