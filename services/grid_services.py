
from domain.entities import grid
from repository.grid_repository import grid_repository

class grid_services:
    def __init__(self, grid_repository):
        # self.__column_count = 7
        # self.__row_count = 6
        # self.__grid = grid(self.__row_count, self.__column_count)
        self.__grid_repository = grid_repository

    def check_if_win(self, player_color):
        # if self.__check_on_rows(player_color) == 'win':
        #     return 'win'
        # if self.__check_on_columns(player_color) == 'win':
        #     return 'win'
        # if self.__check_on_diagonal(player_color) == 'win':
        #     return 'win'
        # return 'false'
        return self.__grid_repository.check_if_win(player_color)


    # def __check_on_rows(self, player_color):
    #     for column_index in range(0, self.__column_count):
    #         column_array = []
    #         for row in self.__grid.matrix:
    #              column_array.append(row[column_index])
    #
    #         for row_index in range(0, self.__row_count - 3):
    #             auxiliar_array = column_array[row_index:row_index + 4]
    #             if auxiliar_array.count(player_color) == 4:
    #                 return 'win'
    #     return 'false'

    # def __check_on_columns(self, player_color):
    #     for row_index in range(0, len(self.__grid.matrix)):
    #         for column_index in range(0, self.__column_count - 3):
    #             row_array = self.__grid.matrix[row_index][column_index:column_index + 4]
    #             if row_array.count(player_color) == 4:
    #                 return 'win'
    #     return 'false'
    #
    # def __check_on_diagonal(self, player_color):
    #     # Check digonals
    #     for row_index in range(0, self.__row_count - 3):
    #         for column_index in range(0, self.__column_count - 3):
    #             diagonal_array = []
    #             for i in range(0, 4):
    #                 diagonal_array.append(self.__grid.matrix[row_index + i][column_index + i])
    #
    #             if diagonal_array.count(player_color) == 4 :
    #                 return 'win'
    #
    #     for row_index in range(0, self.__row_count - 3):
    #         for column_index in range(0, self.__column_count - 3):
    #             diagonal_array = []
    #             for i in range(0, 4):
    #                 diagonal_array.append(self.__grid.matrix[row_index + 3 - i][column_index + i])
    #             if diagonal_array.count(player_color) == 4:
    #                 return 'win'
    #     return 'false'

    # def __add_to_matrix(self, row_index, column_index, player_color):
    #     # self.__grid[row_index][column_index] = player_color
    #     self.__grid_r

    def add_to_grid(self, column_index, player_color):
        # column_index -= 1
        # for row_index in range(len(self.__grid) - 1, -1, -1):
        #     row = self.__grid[row_index]
        #     column_element = row[column_index]
        #     if column_element == self.__grid.zero_element:
        #         self.__add_to_matrix(row_index, column_index, player_color)
        #         return row_index
        # return 'false'
        return self.__grid_repository.add_to_grid(column_index, player_color)

    def get_grid(self):
        #return self.__grid.matrix
        return self.__grid_repository.get_grid()

    def get_board(self):
        #return self.__grid
        return self.__grid_repository.get_board()