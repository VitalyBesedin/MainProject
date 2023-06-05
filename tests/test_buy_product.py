import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import  LoginPage


def test_select_product():
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # g = Service()
    # driver = webdriver.Chrome(options=options, service=g)  # this is and above macOS
    # driver = webdriver.Chrome()  # Windows
    # driver = webdriver.Firefox()
    driver = webdriver.Safari()
    # driver = webdriver.Edge()

    print("Start test")

    login = LoginPage(driver)
    login.authorization()

    enter_shopping_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#shopping_cart_container")))
    enter_shopping_cart.click()
    print("Click Enter Shopping Cart")


    time.sleep(5)

