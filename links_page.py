from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LinksPage:

    # Локаторы
    HOME = (By.ID, "simpleLink")
    HOMELRBTS = (By.ID, "dynamicLink")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def home(self):
        self.wait.until(EC.element_to_be_clickable(self.HOME)).click()

    def homelrbts(self):
        self.wait.until(EC.element_to_be_clickable(self.HOMELRBTS)).click()