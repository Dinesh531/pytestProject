from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def type(self, locator, value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def wait_for_element(self, locator, timeout=10):

        wait = WebDriverWait(self.driver, timeout)

        return wait.until(
            EC.visibility_of_element_located(locator)
        )