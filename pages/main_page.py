from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MainPage(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    select_product_1 = "#add-to-cart-sauce-labs-backpack"
    select_product_2 = "#add-to-cart-sauce-labs-bike-light"
    select_product_3 = "#add-to-cart-sauce-labs-bolt-t-shirt"
    cart = "//span[@class='shopping_cart_badge']"
    main_menu = "#react-burger-menu-btn"
    menu_item_about = "#about_sidebar_link"


    # Getters

    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.select_product_1)))
    def get_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.select_product_2)))
    def get_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.select_product_3)))
    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))
    def get_main_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.main_menu)))
    def get_menu_item_about(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.menu_item_about)))


    def click_product_1(self):
        self.get_product_1().click()
        print("Click product 1")

    def click_product_2(self):
        self.get_product_2().click()
        print("Click product 2")
    def click_product_3(self):
        self.get_product_3().click()
        print("Click product 3")
    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    def click_main_menu(self):
        self.get_main_menu().click()
        print("Click main menu")

    def click_menu_item_about(self):
        self.get_menu_item_about().click()
        print("Click main menu item About")



    # Methods

    def select_product(self):
        self.get_current_url()
        self.click_product_1()
        self.click_cart()

    def select_products_1(self):
        self.get_current_url()
        self.click_product_1()
        self.click_cart()
    def select_products_2(self):
        self.get_current_url()
        self.click_product_2()
        self.click_cart()
    def select_products_3(self):
        self.get_current_url()
        self.click_product_3()
        self.click_cart()
    def select_main_menu_about(self):
        self.get_current_url()
        self.click_main_menu()
        self.click_menu_item_about()
        self.assert_url("https://saucelabs.com/")
        self.get_screenshot()




