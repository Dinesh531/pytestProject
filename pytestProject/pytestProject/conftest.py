import pytest

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService

from utilities.read_config import ReadConfig

@pytest.fixture()
def setup():

    browser = ReadConfig.get_browser()

    if browser == "chrome":

        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            )
        )

    elif browser == "firefox":

        driver = webdriver.Firefox(
            service=FirefoxService(
                GeckoDriverManager().install()
            )
        )

    driver.maximize_window()

    driver.get(
        ReadConfig.get_base_url()
    )

    yield driver

    driver.quit()