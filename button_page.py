from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ButtonPage:

    #Локаторы
    DOUBLE_CLICK_ME = (By.ID, "doubleClickBtn")
    RIGHT_CLICK_ME = (By.ID, "rightClickBtn")
    CLICK_ME = (By.XPATH, "//button[text()='Click Me']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def double_click_me(self):
        self.wait.until(EC.element_to_be_clickable(self.DOUBLE_CLICK_ME)).click()

    def right_click_me(self):
        self.wait.until(EC.element_to_be_clickable(self.RIGHT_CLICK_ME)).click()


    def click_me(self):
        self.wait.until(EC.element_to_be_clickable(self.CLICK_ME)).click()

