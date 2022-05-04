import copy
import os
import sqlite3

from domain.models.config_game import ConfigGame
from domain.models.tick import Tick

cur_dir = os.path.dirname(__file__)
db = os.path.join(cur_dir, '../../stat.sqlite')


def is_cell_live(current_cell, near_living_cells):
    if not current_cell.is_living and near_living_cells == 3:
        register_database('dead_to_life')
        return True
    elif current_cell.is_living and 2 <= near_living_cells <= 3:
        register_database('life_to_life')
        return True
    elif current_cell.is_living:
        register_database('life_to_dead')
        return False
    else:
        register_database('dead_to_dead')
        return False


def register_database(transition):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(f"SELECT {transition} FROM transitions")
    result = c.fetchall()
    c.execute(f"INSERT INTO transitions ({transition})"
              f" VALUES ({result[0][0] + 1})")


class GameService:
    slides: list[Tick]
    config_game: ConfigGame

    def __init__(self) -> None:
        self.slides = []

    def get_slides_game(self, init_game_request):
        self.slides = []
        self.config_game = ConfigGame(init_game_request['size'], init_game_request['ticksNumber'],
                                      init_game_request['liveCellPositions'])
        self.config_game.validate_fields()
        self.slides.append(self.get_initial_tick())
        for i in range(self.config_game.ticks_number):
            new_tick = Tick(i + 1, self.config_game.size)
            new_tick.update_matrix(self.get_tick().matrix_cells)
            self.slides.append(new_tick)
        return self.convert_to_dict()

    def get_initial_tick(self):
        initial_tick = Tick(0, self.config_game.size)
        for position in self.config_game.live_cell_positions:
            row, column = initial_tick.get_row_and_column_by_position(position)
            initial_tick.matrix_cells[row][column].change_state(True)
        return copy.deepcopy(initial_tick)

    def get_tick(self):
        temp_tick = Tick(-1, self.config_game.size)
        for row in range(self.config_game.size):
            for column in range(self.config_game.size):
                temp_tick.matrix_cells[row][column] \
                    .change_state(self.determine_cell_state(row, column))
        return temp_tick

    def determine_cell_state(self, row, column):
        current_cell = copy.deepcopy(self.slides[len(self.slides) - 1].matrix_cells[row][column])
        neighbours = copy.deepcopy(self.slides[len(self.slides) - 1].get_neighbours(row, column))
        near_living_cells = 0
        for cell in neighbours:
            if cell.is_living:
                near_living_cells = near_living_cells + 1
        return is_cell_live(current_cell, near_living_cells)

    def convert_to_dict(self):
        list_dict = []
        for tick in self.slides:
            list_dict.append(tick.to_dict())
        return list_dict
