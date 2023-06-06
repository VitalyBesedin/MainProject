from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class ClientInformationPage(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    first_name = "#first-name"
    last_name = "#last-name"
    zip_code = "#postal-code"
    continue_button = "#continue"



    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.first_name)))
    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.last_name)))
    def get_zip_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.zip_code)))
    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.continue_button)))


    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first name")
    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last name")
    def input_zip_code(self, zip_code):
        self.get_zip_code().send_keys(zip_code)
        print("Input zip code")
    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click product")


    # Methods

    def client_confirmation(self):
        self.get_current_url()
        self.input_first_name("Ivan")
        self.input_last_name("Ivanov")
        self.input_zip_code("111111")
        self.click_continue_button()




