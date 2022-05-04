import copy

from domain.models.cell import Cell


class Tick:
    tick_number: int
    matrix_cells: list

    def __init__(self, tick_number, size) -> None:
        self.tick_number = tick_number
        self.matrix_cells = []
        self._init_matrix(size)

    def _init_matrix(self, size):
        position = 0
        for _ in range(size):
            temp_list = []
            for _ in range(size):
                temp_list.append(Cell(position, False))
                position = position + 1
            self.matrix_cells.append(temp_list)

    def get_neighbours(self, row, column):
        matrix_op = [[-1, -1], (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        neighbours = []
        for ops in matrix_op:
            if len(self.matrix_cells) > row + ops[0] >= 0 and len(self.matrix_cells) > column + ops[1] >= 0:
                neighbours.append(self.matrix_cells[row + ops[0]][column + ops[1]])
        return copy.deepcopy(neighbours)

    def get_row_and_column_by_position(self, position):
        for i in range(len(self.matrix_cells)):
            for j in range(len(self.matrix_cells)):
                if self.matrix_cells[i][j].position == position:
                    return i, j

    def update_matrix(self, new_matrix):
        self.matrix_cells = copy.deepcopy(new_matrix)

    def to_dict(self):
        return {
            "tickNumber": self.tick_number,
            "matrixCells": self.cells_to_array()
        }

    def cells_to_array(self):
        bool_array = []
        for row in self.matrix_cells:
            for cell in row:
                bool_array.append(cell.is_living)
        return bool_array
