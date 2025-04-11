from selenium.webdriver.common.by import By
import selenium.webdriver.chrome
import pytest
from selenium import webdriver


class homePage:
    def __init__(self,driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://demoblaze.com/index.html')

    def clickGalaxyS6(self):
        samsung_s6 = self.driver.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
        samsung_s6.click()

    def clickMonitors(self):
        monitorsPage = self.driver.find_element(By.LINK_TEXT, 'Monitors')
        monitorsPage.click()

    def checkProductsOnPage(self,count):
        monitors = self.driver.find_elements(By.CSS_SELECTOR,  '.card')
        assert len(monitors) == count

    def clickSignUp(self):
        signUp=self.driver.find_element(By.ID, 'signin2')
        signUp.click()






