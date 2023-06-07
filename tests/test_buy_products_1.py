import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.cart_page import CartPage
from pages.client_information_page import ClientInformationPage
from pages.finish_page import FinishPage
from pages.login_page import  LoginPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage

# @pytest.mark.run(order=3)
def test_buy_product_1(set_up):
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # g = Service()
    # driver = webdriver.Chrome(options=options, service=g)  # this is and above macOS
    # driver = webdriver.Chrome()  # Windows
    # driver = webdriver.Firefox()
    driver = webdriver.Safari()
    # driver = webdriver.Edge()

    print("Start Test 1")

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_products_1()

    cp = CartPage(driver)
    cp.product_confirmation()



    cip = ClientInformationPage(driver)
    cip.client_confirmation()

    p = PaymentPage(driver)
    p.payment()

    f = FinishPage(driver)
    f.finish()

    # time.sleep(5)
    print("Finish Test 1")
    driver.quit()

# @pytest.mark.run(order=1)
def test_buy_product_2(set_up):
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # g = Service()
    # driver = webdriver.Chrome(options=options, service=g)  # this is and above macOS
    # driver = webdriver.Chrome()  # Windows
    # driver = webdriver.Firefox()
    driver = webdriver.Safari()
    # driver = webdriver.Edge()

    print("Start Test 2")

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_products_2()

    cp = CartPage(driver)
    cp.product_confirmation()



    # time.sleep(5)
    print("Finish Test 2")
    driver.quit()

# @pytest.mark.run(order=2)
def test_buy_product_3():
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # g = Service()
    # driver = webdriver.Chrome(options=options, service=g)  # this is and above macOS
    # driver = webdriver.Chrome()  # Windows
    # driver = webdriver.Firefox()
    driver = webdriver.Safari()
    # driver = webdriver.Edge()

    print("Start Test 3")

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_products_3()

    cp = CartPage(driver)
    cp.product_confirmation()



    # time.sleep(5)
    print("Finish Test 3")
    driver.quit()
