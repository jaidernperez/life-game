from domain.models.config_game import ConfigGame


class GameService:
    slides_game: list

    def __init__(self) -> None:
        super().__init__()

    def get_slides_game(self, init_game_request):
        config_game = ConfigGame(init_game_request['size'], init_game_request['ticksNumber'],
                                 init_game_request['liveCellPositions'])
        config_game.validate_fields()
        return self._init_default_slides_game()

    def _init_default_slides_game(self):
        return [
            {'tick': 1,
             'matrix': [True, True, True, False, False, True, True, True, False, True, True, False, True, True,
                        True, True, False, True, False, True, False, True, False, True, True]},

            {'tick': 2,
             'matrix': [True, False, False, False, True, True, True, True, True, True, False, True, True, True,
                        True, True, False, True, True, True, False, True, False, True, True]},

            {'tick': 3,
             'matrix': [False, False, False, True, True, False, False, True, True, False, True, True, True, True,
                        True, True, True, False, True, True, True, False, True, True, True]},

            {'tick': 4,
             'matrix': [True, True, False, False, True, True, True, False, False, True, True, False, True, False,
                        True, False, False, True, True, False, True, True, False, False, False]},

            {'tick': 5,
             'matrix': [False, True, True, False, False, True, False, True, True, False, True, False, True, True,
                        True, False, True, True, False, True, True, True, True, True, True]},

            {'tick': 6,
             'matrix': [False, True, False, True, True, True, True, False, True, True, True, True, False, False,
                        False, False, True, False, True, False, True, False, True, True, True]},
        ]
