from Handler import *


class Handler:
    scarping_handler: ScarpingHandler
    file_handler: FileHandler
    response_handler: ResponseHandler

    def __init__(self):
        self.scarping_handler = ScarpingHandler()
        self.file_handler = FileHandler()
        self.response_handler = ResponseHandler()