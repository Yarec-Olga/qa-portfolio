from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class ButtonPage:

    #Локаторы
    DOUBLE_CLICK_ME = (By.ID, "doubleClickBtn")
    RIGHT_CLICK_ME = (By.ID, "rightClickBtn")
    CLICK_ME = (By.XPATH, "//button[text()='Click Me']")

    DOUBLE_CLICK_MESSAGE = (By.ID, "doubleClickMessage")
    RIGHT_CLICK_MESSAGE = (By.ID, "rightClickMessage")
    CLICK_MESSAGE = (By.ID, "dynamicClickMessage")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def double_click_me(self):
        button = self.wait.until(EC.element_to_be_clickable(self.DOUBLE_CLICK_ME))
        ActionChains(self.driver).double_click(button).perform()

    def right_click_me(self):
        button = self.wait.until(EC.element_to_be_clickable(self.RIGHT_CLICK_ME))
        ActionChains(self.driver).context_click(button).perform()


    def click_me(self):
        self.wait.until(EC.element_to_be_clickable(self.CLICK_ME)).click()

    def get_message(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

