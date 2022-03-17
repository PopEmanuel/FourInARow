from domain.entities import *
from services.grid_services import grid_services
from services.computer_services import computer_services
from repository.computer_repo import computer_repository
from repository.grid_repository import grid_repository


class console:

    def __init__(self):

        #self.__grid_service = grid_services()
        self.player_color = 'B'
        self.computer_color = 'R'
        grid_repo = grid_repository()
        computer_repo = computer_repository(self.computer_color, grid_repo.get_board(), grid_repo)
        self.__grid_service = grid_services(grid_repo)
        self.__computer_service = computer_services(computer_repo)

    def start(self):
        """
        Starts the game
        :return:
        """
        self.print_grid()

        while True:
            print("It's BLUE's turn : ")
            if self.take_user_input(self.player_color) != 'false':
                if self.__grid_service.check_if_win(self.player_color) == 'win':
                    print("PLAYER WON")
                    self.print_grid()
                    return
                print("It's RED's turn")
                print(self.__computer_service.make_a_move())
                if self.__grid_service.check_if_win(self.computer_color) == 'win':
                    print("COMPUTER WON")
                    self.print_grid()
                    return

            self.print_grid()

    def take_user_input(self, player_color):
        """
        Takes the user's input and calls the function for adding to the grid
        :param player_color:
        :return:
        """
        column_chosed = input()
        try:
            column_chosed = int(column_chosed)
        except:
            raise ValueError("The column must be int\n")

        if column_chosed > 7:
            print("Invalid column")
            return 'false'

        row_placed = self.__grid_service.add_to_grid(column_chosed, player_color)

        if row_placed == 'false':
            print("The column you are trying to add to is full. Try another one\n")
            return 'false'

    def print_grid(self):
            matrix = self.__grid_service.get_grid()

            row_index = 0
            for row in matrix:
                column_index = 0
                for column in row:
                    print(matrix[row_index][column_index], end=' ')
                    column_index += 1
                print()
                row_index += 1

