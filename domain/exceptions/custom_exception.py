import time


class CustomException(Exception):
    timestamp: float
    status_code: int
    message: str

    def __init__(self, message, status_code=406):
        self.timestamp = time.time()
        self.message = message
        self.status_code = status_code
