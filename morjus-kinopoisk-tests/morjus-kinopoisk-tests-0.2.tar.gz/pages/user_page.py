import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.header_page import HeaderPage
import time


class UserPage(HeaderPage):
    FIRST_MOVIE_IN_LIST = (By.CSS_SELECTOR, '.info .name')
    SELECTION_LISTS = (By.CSS_SELECTOR, 'div .select')
    WATCH_LATER_LIST = (By.CSS_SELECTOR, '.public-folder.slc')

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.base_url = url
        self.movie = None

    def get_first_movie_in_watch_later_list(self):
        with allure.step("Ищу название первого фильма в списке 'Буду смотреть'"):
            movie_name = self.find(locator=self.FIRST_MOVIE_IN_LIST).text
            return movie_name

    def del_first_from_watch_later(self):
        with allure.step("Удаляю первый фильм из списка 'Буду смотреть'"):
            self.find(locator=self.SELECTION_LISTS).click()
            self.find(locator=self.WATCH_LATER_LIST).click()
            time.sleep(1)  # bad practice
            self.driver.refresh()
        with allure.step("Проверяю, что элемент удален"):
            result = self.is_not_element_present(locator=self.FIRST_MOVIE_IN_LIST, time=10)
            return result

    def check_movie_is_not_presented(self):
        res = self.is_not_element_present(locator=self.FIRST_MOVIE_IN_LIST).text
        return res
