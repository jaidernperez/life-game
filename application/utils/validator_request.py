from cerberus import Validator

game_init_schema = {
    'size': {'type': 'integer', 'required': True},
    'ticksNumber': {'type': 'integer', 'required': True},
    'liveCellPositions': {'type': 'list', 'required': True}
}

game_validator = Validator(game_init_schema)
