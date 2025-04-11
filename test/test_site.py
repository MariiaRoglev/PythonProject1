import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.devtools.v134.debugger import pause
import time
from pages.homePage import homePage
from pages.productPage import productPage
from selenium import webdriver
from conftest import driver


def test_open_s6(driver):
    homepage = homePage(driver)
    homepage.open()
    homepage.clickGalaxyS6()

    productpage = productPage(driver)
    productpage.checkTitleIs('Samsung galaxy s6')


def test_open_page_monitors(driver):
    homepage = homePage(driver)
    homepage.open()
    homepage.clickMonitors()

    time.sleep(2)
    homepage.checkProductsOnPage(2)











