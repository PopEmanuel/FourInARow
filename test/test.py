import unittest
from services.grid_services import *
from services.computer_services import *
from repository.grid_repository import grid_repository
from repository.computer_repo import computer_repository

class test_computer(unittest.TestCase):

    def setUp(self):
        grid_repo = grid_repository()
        self.__grid_services = grid_services(grid_repo)
        computer_repo = computer_repository('B', grid_repo.get_board(), grid_repo)

        self.__computer_services = computer_services(computer_repository)

    def test_make_a_move_win_horizontal(self):
        self.__grid_services.add_to_grid(1, 'B')
        self.__grid_services.add_to_grid(1, 'B')
        self.__grid_services.add_to_grid(1, 'B')
        #self.assertEqual(self.__computer_services.make_a_move(), 'computer win')

    def test_make_a_move_win_vertical(self):
        self.__grid_services.add_to_grid(1, 'B')
        self.__grid_services.add_to_grid(2, 'B')
        self.__grid_services.add_to_grid(3, 'B')
        #self.assertEqual(self.__computer_services.make_a_move(), 'computer win')

    def test_make_a_move__win_positive_diagonal(self):
        self.__grid_services.add_to_grid(1, 'B')
        self.__grid_services.add_to_grid(2, 'R')
        self.__grid_services.add_to_grid(2, 'B')
        self.__grid_services.add_to_grid(3, 'B')
        self.__grid_services.add_to_grid(3, 'R')
        self.__grid_services.add_to_grid(3, 'B')
        self.__grid_services.add_to_grid(4, 'B')
        self.__grid_services.add_to_grid(4, 'B')
        self.__grid_services.add_to_grid(4, 'R')
        self.assertEqual(self.__computer_services.make_a_move(), 'computer win')

    def test_make_a_move_negative_win_diagonal(self):
        self.__grid_services.add_to_grid(1, 'R')
        self.__grid_services.add_to_grid(1, 'R')
        self.__grid_services.add_to_grid(1, 'B')
        self.__grid_services.add_to_grid(2, 'R')
        self.__grid_services.add_to_grid(2, 'B')
        self.__grid_services.add_to_grid(2, 'B')
        self.__grid_services.add_to_grid(3, 'B')
        self.__grid_services.add_to_grid(3, 'B')
        self.__grid_services.add_to_grid(4, 'B')
        self.assertEqual(self.__computer_services.make_a_move(), 'computer win')

    def test_make_a_move_random(self):
        self.__grid_services.add_to_grid(1, 'B')
        self.assertEqual(self.__computer_services.make_a_move(), 'random')

    def test_make_a_move_block_horizontal(self):
        self.__grid_services.add_to_grid(7, 'R')
        self.__grid_services.add_to_grid(7, 'R')
        self.__grid_services.add_to_grid(7, 'R')
        self.assertEqual(self.__computer_services.make_a_move(), 'blocked')

    def test_make_a_move_block_vertical(self):
        self.__grid_services.add_to_grid(1, 'R')
        self.__grid_services.add_to_grid(2, 'R')
        self.__grid_services.add_to_grid(3, 'R')
        self.assertEqual(self.__computer_services.make_a_move(), 'blocked')

    def test_make_a_move__block_positive_diagonal(self):
        self.__grid_services.add_to_grid(1, 'R')
        self.__grid_services.add_to_grid(2, 'B')
        self.__grid_services.add_to_grid(2, 'R')
        self.__grid_services.add_to_grid(3, 'R')
        self.__grid_services.add_to_grid(3, 'B')
        self.__grid_services.add_to_grid(3, 'R')
        self.__grid_services.add_to_grid(4, 'R')
        self.__grid_services.add_to_grid(4, 'R')
        self.__grid_services.add_to_grid(4, 'B')
        self.assertEqual(self.__computer_services.make_a_move(), 'blocked')

    def test_make_a_move_negative_block_diagonal(self):
        self.__grid_services.add_to_grid(1, 'B')
        self.__grid_services.add_to_grid(1, 'B')
        self.__grid_services.add_to_grid(1, 'R')
        self.__grid_services.add_to_grid(2, 'B')
        self.__grid_services.add_to_grid(2, 'R')
        self.__grid_services.add_to_grid(2, 'R')
        self.__grid_services.add_to_grid(3, 'R')
        self.__grid_services.add_to_grid(3, 'R')
        self.__grid_services.add_to_grid(4, 'R')
        self.assertEqual(self.__computer_services.make_a_move(), 'blocked')


class test_grid(unittest.TestCase):

    def setUp(self):
        grid_repo = grid_repository()
        self.__grid_service = grid_services(grid_repo)

    def test_check_if_win_horizontal(self):
        self.__grid_service.add_to_grid(1, 'B')
        self.__grid_service.add_to_grid(2, 'B')
        self.__grid_service.add_to_grid(3, 'B')
        self.assertEqual(self.__grid_service.check_if_win('B'), 'false')
        self.__grid_service.add_to_grid(4, 'B')
        self.assertEqual(self.__grid_service.check_if_win('B'), 'win')

    def test_check_if_win_vertical(self):
        self.__grid_service.add_to_grid(1, 'B')
        self.__grid_service.add_to_grid(1, 'B')
        self.__grid_service.add_to_grid(1, 'B')
        self.assertEqual(self.__grid_service.check_if_win('B'), 'false')
        self.__grid_service.add_to_grid(1, 'B')
        self.assertEqual(self.__grid_service.check_if_win('B'), 'win')

    def test_check_if_win_positive_diagonal(self):
        self.__grid_service.add_to_grid(1, 'B')
        self.__grid_service.add_to_grid(2, 'R')
        self.__grid_service.add_to_grid(2, 'B')
        self.__grid_service.add_to_grid(3, 'R')
        self.__grid_service.add_to_grid(3, 'R')
        self.__grid_service.add_to_grid(3, 'B')
        self.__grid_service.add_to_grid(4, 'R')
        self.__grid_service.add_to_grid(4, 'R')
        self.__grid_service.add_to_grid(4, 'R')
        self.assertEqual(self.__grid_service.check_if_win('B'), 'false')
        self.__grid_service.add_to_grid(4, 'B')
        self.assertEqual(self.__grid_service.check_if_win('B'), 'win')

    def test_check_if_win_negative_diagonal(self):
        self.__grid_service.add_to_grid(1, 'R')
        self.__grid_service.add_to_grid(1, 'R')
        self.__grid_service.add_to_grid(1, 'R')
        self.__grid_service.add_to_grid(1, 'B')
        self.__grid_service.add_to_grid(2, 'R')
        self.__grid_service.add_to_grid(2, 'R')
        self.__grid_service.add_to_grid(2, 'B')
        self.__grid_service.add_to_grid(3, 'R')
        self.__grid_service.add_to_grid(3, 'B')
        self.assertEqual(self.__grid_service.check_if_win('B'), 'false')
        self.__grid_service.add_to_grid(4, 'B')
        self.assertEqual(self.__grid_service.check_if_win('B'), 'win')

