import isqrt
import pygame

class SudokuSolver:
    def __init__(self, sudoku, obj):
        self.sudoku = sudoku
        self.count = 0
        self.gui_ob = obj

    def solve_board(self):
        return self.can_solve_board(0, 0, self.sudoku)

    def can_solve_board(self, row, column, board):
        # If the column goes out of bounds, reset it to zero
        if column == len(board[row]):
            column = 0
            row += 1

            # If the new row's index is equal to the board's length then, return true. Since, all rows have been traversed
            if row == len(board):
                return True

        # If the current entry is filled, then move to the next column
        if board[row][column] != 0:
            return self.can_solve_board(row, column + 1, board)

        # Try and check if a value can be placed
        for i in range(1, len(board) + 1):
            value_to_place = i

            if self.can_place_value(row, column, board, value_to_place):
                board[row][column] = value_to_place
                self.gui_ob.update_cell(value_to_place, self.gui_ob.cells[row][column])
                pygame.time.delay(100)

                self.count += 1
                self.print_board(board)

                # Keep going on the current path and check to see if the next values can be placed
                if self.can_solve_board(row, column + 1, board):
                    return True

                board[row][column] = 0

        return False

    def can_place_value(self, row, column, board, value_to_place):
        # Check if valueToPlace conflicts with the other elements in the row
        if value_to_place in board[row]:
            return False

        # Check if valueToPlace conflicts with other elements in the column
        for i in board:
            if i[column] == value_to_place:
                return False

        # Check if valueToPlace conflicts with other elements in the subgrid
        square_size = isqrt.isqrt(len(board))

        start_row = square_size * (row // square_size)
        start_column = square_size * (column // square_size)

        for i in range(start_row, start_row + square_size):
            for j in range(start_column, start_column + square_size):
                if value_to_place == board[i][j]:
                    return False

        return True

    def print_board(self, board):
        for i in board:
            print(i)

        print(f"\n{self.count}\n")

