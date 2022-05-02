from domain.exceptions.custom_exception import CustomException
import domain.utils.constants as constants


class ConfigGame:
    size: int
    ticks_number: int
    live_cell_positions: list

    def __init__(self, size_p, ticks_number_p, live_cell_positions_p) -> None:
        self.size = size_p
        self.ticks_number = ticks_number_p
        self.live_cell_positions = live_cell_positions_p

    def validate_fields(self):
        self._validate_size()
        self._validate_ticks_number()
        self._validate_live_cell_positions()

    def _validate_size(self):
        if not constants.MIN_SIZE <= self.size < constants.MAX_SIZE:
            raise CustomException(constants.SIZE_NOT_VALID, 400)

    def _validate_ticks_number(self):
        if not constants.MIN_TICKS_NUMBER <= self.size < constants.MAX_TICKS_NUMBER:
            raise CustomException(constants.TICKS_NUMBER_NOT_VALID, 400)

    def _validate_live_cell_positions(self):
        if len(self.live_cell_positions) > self.size * self.size:
            raise CustomException(constants.LIVE_CELL_POSITIONS_SIZE_NOT_VALID % (self.size * self.size), 400)
        for position in self.live_cell_positions:
            if not isinstance(position, int):
                raise CustomException(constants.LIVE_CELL_POSITIONS_FORMAT_NOT_VALID, 400)
            elif position >= self.size * self.size:
                raise CustomException(constants.LIVE_CELL_POSITIONS_VALUES_NOT_VALID % (self.size * self.size), 400)
