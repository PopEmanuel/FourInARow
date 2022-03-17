from domain.entities import computer
import random
import copy

class computer_repository:
    def __init__(self, computer_color, board, grid_repository):
        self.__computer = computer(computer_color, board)
        self.__grid_repository = grid_repository
        self.__column_count = 7
        self.__row_count = 6

    def make_a_move(self):
        """
        Calculates which move is best for the computer to do and does it
        :return:
        """
        result = self.check_if_can_win(self.__computer.computer_color)
        if result == 'win':
            return 'computer win'
        result = self.check_if_can_win(self.__computer.player_color)
        if result == 'blocked':
            return 'blocked'

        self.place_random_piece()
        return 'random'

    def place_random_piece(self):
        """
        Places a random piece on the grid
        :return:
        """
        empty_cells = self.get_all_possible_columns(self.__computer.board)
        number = random.randrange(0, len(empty_cells), 1)
        number = empty_cells[number] + 1
        self.__grid_repository.add_to_grid(number, self.__computer.computer_color)

    def check_if_can_win(self, color):
        """
        Verifies if the player with the color 'color' can win the game
        :param color: color of the player (str)
        :return:
        """
        # Check horizontal locations
        for row_index in range(0, len(self.__computer.board.matrix)):
            for column_index in range(0, self.__column_count - 3):
                row_array = self.__computer.board.matrix[row_index][column_index:column_index + 4]
                if row_array.count(color) == 3 and row_array.count(self.__grid_repository.get_board().zero_element) == 1:
                    copy_board = copy.deepcopy(self.__computer.board)
                    array_index = 0
                    for index in range(0, len(row_array)):
                        if row_array[index] == self.__grid_repository.get_board().zero_element:
                            array_index = index
                            array_index += 1
                    array_index += column_index
                    copy_board.add_to_grid(array_index, color)
                    row_array = copy_board.matrix[row_index][column_index:column_index + 4]
                    if row_array.count(color) == 4:
                        if color == self.__computer.computer_color:
                            self.__computer.board.add_to_grid(array_index, color)
                            return 'win'
                        else:
                            self.__computer.board.add_to_grid(array_index, self.__computer.computer_color)
                            return 'blocked'

        # Check vertical locations
        for column_index in range(0, self.__column_count):
            column_array = []
            for row in self.__computer.board.matrix:
                #try:
                column_array.append(row[column_index])
                # except:
                #     print(column_index, len(row))

            for row_index in range(0, self.__row_count - 3):
                auxiliar_array = column_array[row_index:row_index + 4]
                if auxiliar_array.count(color) == 3 and auxiliar_array.count(self.__grid_repository.get_board().zero_element) == 1:
                    if color == self.__computer.computer_color:
                        self.__computer.board.add_to_grid(column_index + 1, color)
                        return 'win'
                    else:
                        self.__computer.board.add_to_grid(column_index + 1, self.__computer.computer_color)
                        return 'blocked'

        # Check digonals
        for row_index in range(0, self.__row_count - 3):
            for column_index in range(0, self.__column_count - 3):
                diagonal_array = []
                for i in range(0, 4):
                    diagonal_array.append(self.__computer.board.matrix[row_index + i][column_index + i])

                if diagonal_array.count(color) == 3 and diagonal_array.count(self.__grid_repository.get_board().zero_element) == 1:
                    copy_board = copy.deepcopy(self.__computer.board)
                    array_index = 0
                    for index in range(0, len(diagonal_array)):
                        if diagonal_array[index] == self.__grid_repository.get_board().zero_element:
                            array_index = index
                    array_index += column_index + 1
                    copy_board.add_to_grid(array_index, color)
                    diagonal_array = []
                    for i in range(0, 4):
                        diagonal_array.append(copy_board.matrix[row_index + i][column_index + i])
                    if diagonal_array.count(color) == 4:
                        if color == self.__computer.computer_color:
                            self.__computer.board.add_to_grid(array_index, color)
                            return 'win'
                        else:
                            self.__computer.board.add_to_grid(array_index, self.__computer.computer_color)
                            return 'blocked'

        for row_index in range(0, self.__row_count - 3):
            for column_index in range(0, self.__column_count - 3):
                diagonal_array = []
                for i in range(0, 4):
                    diagonal_array.append(self.__computer.board.matrix[row_index + 3 - i][column_index + i])
                if diagonal_array.count(color) == 3 and diagonal_array.count(self.__grid_repository.get_board().zero_element) == 1:
                    copy_board = copy.deepcopy(self.__computer.board)
                    array_index = 0
                    print(diagonal_array)
                    for index in range(0, len(diagonal_array)):
                        if diagonal_array[index] == self.__grid_repository.get_board().zero_element:
                            array_index = index
                    array_index += column_index + 1
                    copy_board.add_to_grid(array_index, color)

                    print(array_index, column_index + 1)
                    diagonal_array = []
                    for i in range(0, 4):
                        diagonal_array.append(copy_board.matrix[row_index + 3 - i][column_index + i])
                    print("da", diagonal_array)
                    if diagonal_array.count(color) == 4:
                        if color == self.__computer.computer_color:
                            self.__computer.board.add_to_grid(array_index , color)
                            return 'win'
                        else:
                            self.__computer.board.add_to_grid(array_index , self.__computer.computer_color)
                            return 'blocked'
        return 'false'

    def get_all_possible_columns(self, board):
        """
        Gets all the columns which are still free for placing a piece
        :param board: the grid with all elements
        :return:
        """
        list = []
        row = board.matrix[0]
        for index in range(0, len(row)):
            if row[index] == self.__grid_repository.get_board().zero_element:
                list.append(index)

        return list