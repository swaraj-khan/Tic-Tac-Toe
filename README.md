# Tic-Tac0Toe

This is a simple implementation of the classic game Tic Tac Toe using Python's Tkinter GUI library. The game can be played by a human player against a computer AI.

Prerequisites

    -Python 3
    -Tkinter library
  
How to run the game


    -To run the game, simply execute the tictactoe.py file in your Python environment.

Game rules


    -The game is played on a 3x3 grid.
    -Player 1 uses "X" and player 2 (the computer) uses "O".
    -Players take turns placing their marks on an empty cell on the board.
    -The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins the game.
    -If all cells on the board are filled and no player has won, the game ends in a draw.
  
  
Code structure


     -The TicTacToe class represents the game board and provides methods to check for a win, a draw, and to evaluate the state of the board.
     -The minimax algorithm is used to determine the best move for the computer player.
     -The GUI is implemented using Tkinter, with buttons representing the cells on the board and labels for the status of the game and the scores of the players.
