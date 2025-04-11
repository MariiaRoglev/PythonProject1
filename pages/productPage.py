from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver

class productPage:
    def __init__(self,driver):
        self.driver = driver

    def checkTitleIs(self,title):
        pageTitle = self.driver.find_element(By.CSS_SELECTOR, 'h2')
        assert pageTitle.text == title





