import requests
from Handler.File import *


class ResponseHandler:
    file_handler: FileHandler

    def __init__(self):
        self.file_handler = FileHandler()

    def request(self, url):
        field_name = ['url', 'status_code', 'Error']
        error_data = {
            'url': url,
            'status_code': 0,
            'Error': ''
        }

        try:
            response = requests.get(url)
            status_code = response.status_code
            if response.ok and response.status_code == 200:
                return response
            else:
                print(response.ok)
                error_data['status_code'] = response.status_code
                self.file_handler.append_data_csv('Error',
                                                  error_data,
                                                  field_name)
                return
        except requests.RequestException as e:
            print(e)
            error_data['Error'] = e
            self.file_handler.append_data_csv('Error',
                                              error_data,
                                              field_name)
