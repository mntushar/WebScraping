import requests
from Handler.File import *


class ResponseHandler:
    file_handler: FileHandler

    def __init__(self): ...

    def request(self, url): ...
