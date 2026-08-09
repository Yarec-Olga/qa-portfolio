from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TextBoxPage:

    USERNAME = (By.ID, "userName")
    EMAIL = (By.ID, "userEmail")
    SUBMIT = (By.ID, "submit")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def fill_username(self, name):
        self.wait.until(EC.presence_of_element_located(self.USERNAME)).send_keys(name)

    def fill_email(self, email):
        self.wait.until(EC.presence_of_element_located(self.EMAIL)).send_keys(email)

    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT)).click()
