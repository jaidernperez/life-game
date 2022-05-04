class Cell:
    position: int
    is_living: bool

    def __init__(self, position, is_living) -> None:
        self.position = position
        self.is_living = is_living

    def change_state(self, state):
        self.is_living = state
