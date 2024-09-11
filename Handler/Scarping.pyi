import requests
from selenium import webdriver


class ScarpingHandler:
    @staticmethod
    def beautiful_soup_create(response: requests.Response): ...

    @staticmethod
    def selenium_create(): ...

    @staticmethod
    def check_xpath(driver:  webdriver, path: str): ...
