import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.devtools.v134.debugger import pause
import time
from pages.homePage import homePage
from pages.productPage import productPage
from selenium import webdriver
from conftest import driver
from pages.signUp import signUp



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


def test_signup(driver):
    homepage = homePage(driver)
    homepage.open()
    homepage.clickSignUp()

def test_SignUpValidData(driver):
    homepage = homePage(driver)
    homepage.open()
    homepage.clickSignUp()

    time.sleep(2)
    signup = signUp (driver)
    signup.enterUserNameAndPwd()

def test_close_signUpForm(driver):
    homepage = homePage(driver)
    homepage.open()
    homepage.clickSignUp()

    time.sleep(2)
    signup = signUp(driver)
    signup.closeSignIn()















