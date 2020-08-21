import allure
from selenium.webdriver.common.by import By
from pages.header_page import HeaderPage


class MoviePage(HeaderPage):

    STARS = (By.CSS_SELECTOR, '[name="star"]+span')
    MY_RATING = (By.CSS_SELECTOR, 'div h4+span')
    DELETE_RATING = (By.XPATH, '//button[contains(text(), "Удалить")]')
    WATCH_LATER = (By.XPATH, '//button[contains(text(), "Буду смотреть")]')
    WATCH_LATER_LINK = (By.XPATH, '//a[contains(text(), "Буду смотреть")]')
    WATCH_LATER_HEADER = (By.XPATH, '//p/span[contains(text(), "Буду смотреть")]')
    MOVIE_NAME = (By.XPATH, '//h1/span[contains(text(), "")]')
    FIRST_MOVIE_IN_LIST = (By.CSS_SELECTOR, '.info .name')

    TRAILERS = (By.CSS_SELECTOR, '.film-trailer [role="button"]')
    IFRAME_TRAILER = (By.CSS_SELECTOR, 'div .discovery-trailers-wrapper iframe')
    MOVIE_NAME_IN_IFRAME = (By.XPATH, '//a[contains (@href, "player")][contains(text(), "")][@class]') #a[href$="player"]  [contains (@href, "player")]

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.base_url = url

        self.number = None
        self.movie_name = None

    def get_movie_name(self):
        with allure.step("Выставляю русское имя фильма из заголовка в атрибуты объекта"):
            movie_name = self.find(locator=self.MOVIE_NAME).text
            self.movie_name = movie_name
            return movie_name

    def set_rating(self, number: int):
        self.number = number
        self.movie_name = self.get_movie_name()

        with allure.step("Поиск звезд для выставления рейтинга"):
            stars = self.finds(locator=self.STARS)
        with allure.step(f"Выставляю фильму рейтинг {self.number}"):
            stars[number-1].click()

    def check_rating_on_page(self):
        with allure.step("Ищу выставленную оценку на странице"):
            rating = self.find(locator=self.MY_RATING).text
            return rating

    def delete_rating_on_page(self):
        with allure.step("Ищу кнопку удаления оценки и нажимаю"):
            self.find(locator=self.DELETE_RATING).click()
        with allure.step("Удаляю оценку"):
            self.find(locator=self.DELETE_RATING).click()

    def check_rating_is_not_presented(self):
        res = self.is_not_element_present(locator=self.MY_RATING)
        return res

    def add_to_watch_later(self):
        with allure.step("Ищу кнопку добавления в список 'Буду смотреть' и нажимаю"):
            self.find(locator=self.WATCH_LATER).click()

    def go_to_watch_later_list(self):
        with allure.step("Ищу ссылку на список 'Буду смотреть' и нажимаю"):
            self.find(locator=self.WATCH_LATER_LINK).click()
        with allure.step("Ищу заголовок страницы 'Буду смотреть'"):
            self.find(locator=self.WATCH_LATER_HEADER)

    def open_trailer(self):
        with allure.step("Ищу трейлеры на странице и нажимаю на самый первый"):
            self.find(locator=self.TRAILERS).click()
        with allure.step("Переключаюсь на iframe"):
            # import time
            # time.sleep(40)
            iframe = self.find(locator=self.IFRAME_TRAILER)

            self.driver.switch_to.frame(iframe)
        with allure.step("Ищу заголовок фильма"):
            return self.find(locator=self.MOVIE_NAME_IN_IFRAME).text
