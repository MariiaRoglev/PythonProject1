from selenium.webdriver.common.by import By
import selenium.webdriver.chrome
import pytest
from selenium import webdriver
from selenium.webdriver.common.devtools.v133.debugger import pause
from selenium.webdriver.support.wait import WebDriverWait
import time


class signUp:
    def __init__(self,driver):
        self.driver = driver

    def enterUserNameAndPwd(self):
        name = self.driver.find_element(By.ID, 'sign-username').send_keys('Maria')
        pwd = self.driver.find_element(By.ID, 'sign-password').send_keys('Qwerty1!')

        clickSignUpBtn = self.driver.find_element(By.XPATH, '//button[text()="Sign up"]').click()

    def closeSignIn(self):
        closeBtn = self.driver.find_element(By.XPATH, '//button[text()="Close"]')


