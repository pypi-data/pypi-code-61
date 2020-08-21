import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import logging
from dotenv import load_dotenv
from allure_commons.types import AttachmentType

load_dotenv()
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename="test.log")


class ScreenshotListener(AbstractEventListener):

    def before_click(self, element, driver):
        logging.info(f"I'm clicking {element}")

    def after_click(self, element, driver):
        logging.info(f"I've clicked {element}")

    def before_find(self, by, value, driver):
        logging.info(f"I'm looking for '{value}' with '{by}'")

    def after_find(self, by, value, driver):
        logging.info(f"I've found '{value}' with '{by}'")

    def before_quit(self, driver):
        logging.info(f"I'm getting ready to terminate {driver}")

    def after_quit(self, driver):
        logging.info(f"Driver closed.")

    def on_exception(self, exception, driver):
        logger.error(f'Oooops i got: {exception}')
        allure.attach(driver.get_screenshot_as_png(), name=f"{driver.session_id}.png",
                      attachment_type=AttachmentType.PNG)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--selenoid", action="store", default="172.17.0.2")  # localhost


@pytest.fixture(scope="function")
def browser(request):
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--ignore-certificate-errors')
    # options.add_argument("--headless")
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'browser': 'ALL'}
    browser = EventFiringWebDriver(webdriver.Chrome(
        options=options, desired_capabilities=d
    ), ScreenshotListener())
    with allure.step("Start chrome browser for test."):

        def fin():
            try:
                allure.attach(name=browser.session_id,
                              body=str(browser.desired_capabilities),
                              attachment_type=allure.attachment_type.JSON)
                allure.attach(name="chrome log",
                              body=browser.get_log('browser'),
                              attachment_type=allure.attachment_type.TEXT)
            except TypeError as e:
                logger.error(f'Oooops i got: {e}')
            finally:
                with allure.step("Closing browser."):
                    browser.quit()

        request.addfinalizer(fin)
        return browser
