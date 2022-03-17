import pygame
from domain.entities import grid, computer
import sys
from services.grid_services import grid_services
from services.computer_services import computer_services
from repository.grid_repository import grid_repository
from repository.computer_repo import computer_repository

class gui:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.__column_count = 7
        self.__square_size = 100
        self.__row_count = 6
        self.__game_over = False
        self.__size = (self.__column_count * 100, (self.__row_count + 1) * 100)
        self.__screen = pygame.display.set_mode(self.__size)
        grid_repo = grid_repository()
        self.__grid_service = grid_services(grid_repo)
        self.__board = self.__grid_service.get_board()
        self.__mouse_position = [0, 0]
        self.__turn = 'R'
        self.__computer_color = 'B'
        self.__player_color = 'R'
        computer_repo = computer_repository(self.__computer_color, grid_repo.get_board(), grid_repo)
        self.__computer_service = computer_services(computer_repo)
        self.__zero_element = self.__grid_service.get_board().zero_element

    def draw_board(self):
        """
        Draws the board using pygame built-in functions
        :return:
        """
        yellow = (255, 255, 0)
        red = (255, 0, 0)
        blue = (0, 0, 255)
        black = (0, 0, 0)
        pygame.draw.rect(self.__screen, black, (0, 0, self.__column_count * 100, (self.__row_count  + 1) * 100))
        if self.__turn == 'R':
            pygame.draw.circle(self.__screen, red, (self.__mouse_position[0], 50), self.__square_size / 2 - 10)
        else:
            pygame.draw.circle(self.__screen, blue, (self.__mouse_position[0], 50), self.__square_size / 2 - 10)
        for column in range(self.__column_count):
            for row in range(0, self.__row_count):
                pygame.draw.rect(self.__screen, yellow, (column * self.__square_size, row * self.__square_size + self.__square_size, self.__square_size, self.__square_size))
                if self.__grid_service.get_grid()[row][column] == self.__zero_element:
                    pygame.draw.circle(self.__screen, black, (column * self.__square_size + self.__square_size / 2, row * self.__square_size + self.__square_size + self.__square_size / 2)
                                       , self.__square_size / 2 - 10)
                elif self.__grid_service.get_grid()[row][column] == 'R':
                    pygame.draw.circle(self.__screen, red, (
                    column * self.__square_size + self.__square_size / 2, row * self.__square_size + self.__square_size + self.__square_size / 2)
                                       , self.__square_size / 2 - 10)
                elif self.__grid_service.get_grid()[row][column] == 'B':
                    pygame.draw.circle(self.__screen, blue, (
                        column * self.__square_size + self.__square_size / 2, row * self.__square_size + self.__square_size + self.__square_size / 2)
                                       , self.__square_size / 2 - 10)

    def start(self):
        """
        Starts the game
        :return:
        """
        while not self.__game_over:
            self.draw_board()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    position_x = event.pos[0]
                    column = int(position_x // self.__square_size)
                    available_columns = self.__computer_service.get_all_possible_columns(self.__board)

                    if column in available_columns:
                        if self.__turn == 'B':
                            self.__grid_service.add_to_grid(column + 1, 'B')
                            self.__turn = 'R'
                        else:
                            self.__grid_service.add_to_grid(column + 1, 'R')
                            self.__turn = 'B'

                        print(self.__computer_service.make_a_move())

                        if self.__turn == 'B':
                            self.__turn = 'R'
                        else:
                            self.__turn = 'B'

                    if self.__grid_service.check_if_win(self.__player_color) == 'win':
                        print("Player WON")
                        self.draw_board()
                        pygame.display.update()
                        pygame.time.wait(5000)
                        self.__game_over = True

                    print("It's RED's turn")
                    if self.__grid_service.check_if_win(self.__computer_color) == 'win':
                        print("Computer WON")
                        self.draw_board()
                        pygame.display.update()
                        pygame.time.wait(5000)
                        self.__game_over = True

                if event.type == pygame.MOUSEMOTION:
                    self.__mouse_position = event.pos


