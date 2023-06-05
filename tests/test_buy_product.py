import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import  LoginPage
from pages.main_page import MainPage


def test_buy_product():
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # g = Service()
    # driver = webdriver.Chrome(options=options, service=g)  # this is and above macOS
    # driver = webdriver.Chrome()  # Windows
    # driver = webdriver.Firefox()
    # driver = webdriver.Safari()
    driver = webdriver.Edge()

    print("Start test")

    login = LoginPage(driver)
    login.authorization()
    mp = MainPage(driver)
    mp.select_product()



    time.sleep(5)

