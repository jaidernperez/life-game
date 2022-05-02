import time

WELCOME = {'timestamp': time.time(), 'message': 'welcome to the simulator lifegame API!'}
INVALID_REQUEST = {'timestamp': time.time(), 'message': 'request not valid'}
NOT_FOUND_ENDPOINT = {'timestamp': time.time(), 'message': 'the path is not valid'}
INTERNAL_SERVER_ERROR = {'timestamp': time.time(), 'message': 'a unexpected error has occurred'}
