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
    cart = "//span[@class='shopping_cart_badge']"


    # Getters

    def get_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.select_product_1)))
    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))


    def click_product(self):
        self.get_product().click()
        print("Click product")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")



    # Methods

    def select_product(self):
        self.get_current_url()
        self.click_product()
        self.click_cart()




