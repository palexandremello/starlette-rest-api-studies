class ServerError(Exception):
    def __init__(self, error: Exception):
        self.error = error
        self.message = 'ServerError'
        super().__init__(self.error, self.message)