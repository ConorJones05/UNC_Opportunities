import numpy as np
import random
import sympy as sy
import matplotlib.pyplot as plt
from datascience import *

class BattleshipGame:
    def __init__(self):
        self.board = np.repeat(0, 100)
        self.carrier = 5
        self.battleship = 4
        self.cruiser = 3
        self.submarine = 3
        self.patrol_boat = 2
        self.ships = [self.carrier, self.battleship, self.cruiser, self.submarine, self.patrol_boat]

    def horizontal(self, ship_choice):
        while True:
            choice_y = random.choice(np.arange(0, 10))
            choice_x = random.choice(np.arange(1, 12 - ship_choice))
            choice = choice_x + choice_y * 10
            if all(0 <= choice + i < len(self.board) and self.board[choice + i] == 0 for i in range(ship_choice)):
                for i in range(ship_choice):
                    self.board[choice + i] = 1
                return self.board, choice

    def vertical(self, ship_choice):
        while True:
            choice_y = random.choice(np.arange(0, 11 - ship_choice))
            choice_x = random.choice(np.arange(0, 10))
            choice = choice_x + choice_y * 10
            if all(0 <= choice + i < len(self.board) and self.board[choice + (i*10)] == 0 for i in range(ship_choice)):
                for i in range(ship_choice):
                    self.board[choice + (i-1)*10] = 1
                return self.board, choice

    def build_board(self):
        ship_order = random.sample(self.ships, 5)
        vert_hor_order = [random.choice([0, 1]) for i in range(5)]
        for i in range(5):
            if vert_hor_order[i] == 0:
                self.horizontal(ship_order[i])
            else:
                self.vertical(ship_order[i])
        return self.board

    def game_logic(self, pick):
        if self.board[pick] == 1:
            self.board[pick] = 2

BattleshipGame().build_board()