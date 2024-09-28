class RecordNotFound(Exception):
    def __init__(self, message):
        self.message = "Record Not Found"
        super().__init__(message)