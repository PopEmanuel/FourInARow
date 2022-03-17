import copy
import random

class grid:

    def __init__(self, rows, columns):
        self.__columns = columns
        self.__rows = rows
        self.__matrix = []
        self.zero_element = '_'
        self.__matrix = self.__make_matrix_null(self.__matrix, rows, columns)

    def __make_matrix_null(self, matrix, rows, columns):
        matrix.clear()
        for indexi in range(0, rows):
            row = []
            for indexj in range(0, columns):
                row.append(self.zero_element)
            matrix.append(row)
        return matrix

    def add_to_grid(self, column_index, player_color):
        column_index -= 1
        for row_index in range(len(self.__matrix) - 1, -1, -1):
            row = self.__matrix[row_index]
            column_element = row[column_index]
            if column_element == self.zero_element:
                self.__add_to_matrix(row_index, column_index, player_color)
                return row_index
        return 'false'

    def __add_to_matrix(self, row_index, column_index, player_color):
        self.__matrix[row_index][column_index] = player_color

    def __getitem__(self, index):
        return self.__matrix[index]

    def __len__(self):
        return len(self.__matrix)

    @property
    def matrix(self):
        return self.__matrix

class computer:
    def __init__(self, color, bboard):
        self.computer_color = color
        self.board = bboard
        if self.computer_color == 'B':
            self.player_color = 'R'
        else:
            self.player_color = 'B'
