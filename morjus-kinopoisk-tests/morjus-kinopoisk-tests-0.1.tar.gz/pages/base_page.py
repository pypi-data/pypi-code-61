from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
import time
import os
import allure
from dotenv import load_dotenv
load_dotenv()


class BasePage:

    def __init__(self, driver, url=None):
        self.driver = driver
        self.base_url = url

    def find(self, locator, time=10):
        with allure.step(f"Поиск элемента, {locator}"):
            return WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(locator),
                message=f"Can't find element by locator {locator}")

    def find_interactable(self, locator, time=10):
        with allure.step(f"Поиск интерактивного элемента, {locator}"):
            return WebDriverWait(self.driver, time).until(
                EC.element_to_be_clickable(locator),
                message=f"Can't find element by locator {locator}")

    def finds(self, locator, time=10):
        with allure.step(f"Поиск элементов, {locator}"):
            return WebDriverWait(self.driver, time).until(
                EC.presence_of_all_elements_located(locator),
                message=f"Can't find elements by locator {locator}")

    def is_element_present(self, locator, time=10):
        with allure.step(f"Поиск видимых элементов на странице, {locator}"):
            try:
                WebDriverWait(self.driver, time).until(
                    EC.visibility_of_element_located(locator),
                    message=f"Can't find elements by locator {locator}")
            except NoSuchElementException:
                return False
            return True

    def is_not_element_present(self, locator, time=10):
        with allure.step(f"Поиск элемента, которого не должно быть на странице, {locator}"):
            try:
                WebDriverWait(self.driver, time).until(
                    EC.presence_of_element_located(locator),
                    message=f"Can find elements by locator {locator}")
            except TimeoutException:
                return True
            return False

    def is_disappeared(self, locator, time=1):
        with allure.step(f"Поиск элемента, которого должен пропасть, {locator}"):
            try:
                WebDriverWait(self.driver, time, 1, TimeoutException).\
                    until_not(EC.presence_of_element_located(locator))
            except TimeoutException:
                return False
            return True

    def open(self):
        with allure.step(f"Переход на страницу, {self.base_url}"):
            return self.driver.get(self.base_url)


