"""This module implements the Minesweeper game."""

import random


class Minesweeper:
    def __init__(self, rows: int, cols: int, num_mines: int):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.board = [["" for _ in range(cols)] for _ in range(rows)]
        self.mines = set()
        self.revealed = set()
        self.place_mines()

    def place_mines(self):
        """Randomly place mines on the board, updating adjacent cells with mine counts."""
        while len(self.mines) < self.num_mines:
            r, c = random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)
            if (r, c) not in self.mines:
                self.mines.add((r, c))
                self.board[r][c] = "💣"

        for r, c in self.mines:
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if (
                        0 <= i < self.rows
                        and 0 <= j < self.cols
                        and self.board[i][j] != "💣"
                    ):
                        if self.board[i][j] == "":
                            self.board[i][j] = 1
                        else:
                            self.board[i][j] += 1
        pass

    def reveal(self, row: int, col: int) -> str:
        """Reveal a cell on the board.
        Any adjacent cells with no mines are also revealed.
        Returns "Game Over" if a mine is revealed, "Continue" otherwise.
        """
        if (row, col) in self.mines:
            return "Game Over"

        if (row, col) in self.revealed:
            return "Continue"

        self.revealed.add((row, col))
        if self.board[row][col] == "":
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if 0 <= i < self.rows and 0 <= j < self.cols:
                        self.reveal(i, j)

        return "Continue"

    def get_board(self) -> list:
        """Return the current state of the board."""
        board = []
        for row in range(len(self.board)):
            new_row = []
            for col in range(len(self.board[0])):
                value = self.board[row][col] if (row, col) in self.revealed else "?"
                new_row.append(value)
            board.append(new_row)

        return board

    def is_winner(self) -> bool:
        """Check if the game has been won."""
        return len(self.revealed) == self.rows * self.cols - self.num_mines

    def restart(self) -> None:
        """Restart the game with the same parameters."""
        self.__init__(self.rows, self.cols, self.num_mines)


random.seed(0)
minesweeper = Minesweeper(3, 3, 2)
# minesweeper.place_mines()
minesweeper.reveal(2, 2)
print(minesweeper.board)
