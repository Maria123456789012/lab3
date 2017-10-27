class RequestError(IndexError):
    def __init__(self, message):
        self.message = message
