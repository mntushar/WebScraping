from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By


class ScarpingHandler:
    @staticmethod
    def beautiful_soup_create(response: requests.Response):
        if response:
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup

    @staticmethod
    def selenium_create():
        driver = webdriver.Chrome()
        return driver

    @staticmethod
    def check_xpath(driver, path):
        try:
            element = driver.find_element(By.XPATH, path)
            if element:
                return True
        except Exception as e:
            print(e)
            return False

