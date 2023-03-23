import tkinter as tk
import math
import random

# Constants
X = "X"
O = "O"
EMPTY = None
# Scores:


class TicTacToe:
    def __init__(self, p=0, c=0, d=0):
        # Initialize the board
        self.board = [[EMPTY, EMPTY, EMPTY],
                      [EMPTY, EMPTY, EMPTY],
                      [EMPTY, EMPTY, EMPTY]]

        # Initialize the player
        self.player = X
        self.pScore = p
        self.cScore = c
        self.dScore = d

    def empty_cells(self):
        # Return a list of empty cells in the board
        cells = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == EMPTY:
                    cells.append((i, j))
        return cells

    def check_win(self, player):
        # Check if the given player has won the game
        for i in range(3):
            if (self.board[i][0] == player and self.board[i][1] == player and self.board[i][2] == player):
                return True
            if (self.board[0][i] == player and self.board[1][i] == player and self.board[2][i] == player):
                return True
        if (self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player):
            return True
        if (self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player):
            return True
        return False

    def check_draw(self):
        # Check if the game is a draw
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == EMPTY:
                    return False
        return True

    def evaluate(self):
        # Evaluate the current state of the board
        if self.check_win(X):
            return -1
        elif self.check_win(O):
            return 1
        else:
            return 0

    def minimax(self, depth, player):
        # Implement the minimax algorithm to determine the best move for the computer
        if player == O:
            best = [-1, -1, -math.inf]
        else:
            best = [-1, -1, math.inf]

        if depth == 0 or self.check_win(X) or self.check_win(O) or self.check_draw():
            score = self.evaluate()
            return [-1, -1, score]

        for cell in self.empty_cells():
            i, j = cell
            self.board[i][j] = player
            score = self.minimax(depth - 1, O if player == X else X)
            self.board[i][j] = EMPTY
            score[0], score[1] = i, j

            if player == O:
                if score[2] > best[2]:
                    best = score
            else:
                if score[2] < best[2]:
                    best = score

        return best

    def play(self, i, j):
        # Check if the cell is already occupied
        if self.board[i][j] != EMPTY:
            return

    # Player's move
        if not self.check_win(X) and not self.check_win(O):
            self.board[i][j] = self.player
            self.player = O

            if self.check_win(X):
                self.status_label.config(text="You win!")
                self.pScore += 1
                self.scores.config(
                    text=f"Player(X): {self.pScore} Computer(O): {self.cScore} Draw: {self.dScore}")
                pattern = self.get_winning_pattern(O)
                pattern = self.get_winning_pattern(X)
                self.highlight_winning_pattern(pattern, X)

            elif self.check_draw():
                self.status_label.config(text="It's a draw!")
                # Update the GUI board
                self.cells[i][j].config(text=X)
                self.dScore += 1
                self.scores.config(
                    text=f"Player(X): {self.pScore} Computer(O): {self.cScore} Draw: {self.dScore}")
                pattern = self.get_winning_pattern(O)
                pattern = self.get_winning_pattern(X)
                self.highlight_winning_pattern(pattern, X)

            else:
                self.status_label.config(text="")

        # Computer's move
        depth = len(self.empty_cells())
        if depth == 0 or self.check_win(X) or self.check_win(O) or self.check_draw():
            return
        else:
            self.status_label.config(text="Computer thinking...")
            i, j, score = self.minimax(depth, O)
            self.board[i][j] = O
            self.player = X
            if self.check_win(O):
                self.status_label.config(text="Computer wins!")

                self.cScore += 1
                self.scores.config(
                    text=f"Player(X): {self.pScore} Computer(O): {self.cScore} Draw: {self.dScore}")
                pattern = self.get_winning_pattern(O)
                self.highlight_winning_pattern(pattern, O)
            elif self.check_draw():
                self.status_label.config(text="It's a draw!")
                self.dScore += 1
                self.scores.config(
                    text=f"Player(X): {self.pScore} Computer(O): {self.cScore} Draw: {self.dScore}")
                pattern = self.get_winning_pattern(O)
                pattern = self.get_winning_pattern(O)
                self.highlight_winning_pattern(pattern, O)

            else:
                self.status_label.config(text="")

        # Update the GUI board
        for i in range(3):
            for j in range(3):
                self.cells[i][j].config(text=self.board[i][j])

    def get_winning_pattern(self, symbol):
        # Check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == symbol:
                return [(i, 0), (i, 1), (i, 2)]

        # Check columns
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] == symbol:
                return [(0, j), (1, j), (2, j)]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol:
            return [(0, 0), (1, 1), (2, 2)]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == symbol:
            return [(0, 2), (1, 1), (2, 0)]

        return None

    def highlight_winning_pattern(self, pattern, symbol):
        if pattern is None:
            for i in range(3):
                for j in range(3):
                    self.cells[i][j].config(bg="yellow")
        else:
            for i, j in pattern:
                if symbol == X:
                    self.cells[i][j].config(bg="Green")
                else:
                    self.cells[i][j].config(bg="red")

    def reset_board(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.winner = None
        self.status_label.configure(text="")
        for row in self.cells:
            for cell in row:
                cell.configure(text="", state=tk.NORMAL, bg='#f1f0f1')
        self.__init__(self.pScore, self.cScore, self.dScore)

    def create_board(self):
        # Create the GUI board
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.cells = []
        for i in range(3):
            row = []
            for j in range(3):
                cell = tk.Button(self.window, text="", font=("consolas", 32), width=5, height=2,
                                 command=lambda i=i, j=j: self.play(i, j))
                cell.grid(row=i, column=j)
                row.append(cell)
            self.cells.append(row)

        self.status_label = tk.Label(self.window, text="")
        self.status_label.grid(row=3, column=0, columnspan=3)

        # Create a button widget
        button = tk.Button(self.window, text="New Game", font=(
            "consolas", 16), command=self.reset_board)
        button.grid(row=4, column=0, columnspan=3)

        self.scores = tk.Label(
            self.window, text=f"Player(X): {self.pScore} Computer(O): {self.cScore} Draw: {self.dScore}")
        self.scores.grid(row=5, column=0, columnspan=3)
        self.window.mainloop()


game = TicTacToe()
game.create_board()
