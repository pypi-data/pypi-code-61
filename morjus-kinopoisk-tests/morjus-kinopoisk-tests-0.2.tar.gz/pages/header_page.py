import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HeaderPage(BasePage):
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#passp-field-login')
    PASSW_FIELD = (By.CSS_SELECTOR, '#passp-field-passwd')
    SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')
    SKIP_PHONE_BUTTON = (By.XPATH, '//button[@type="button"]')

    SEARCH_FIELD = (By.CSS_SELECTOR, "input[type='text']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')

    HD_LINK = (By.XPATH, '//a[contains(text(), "Онлайн-кинотеатр")]')
    MY_BUYS = (By.XPATH, '//a[contains(text(), "Мои покупки")]')

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.base_url = url

    def _set_email(self, email):
        with allure.step(f"Отправка {email} в {self.EMAIL_FIELD}"):
            self.find(locator=self.EMAIL_FIELD).send_keys(email)

    def _set_passw(self, passw):
        with allure.step(f"Отправка {passw} в {self.PASSW_FIELD}"):
            self.find(locator=self.PASSW_FIELD).send_keys(passw)

    def login(self, email, passw):
        with allure.step(f"Нажатие на 'Войти' на главной странице"):
            self.find(locator=self.LOGIN_BUTTON).click()
        self._set_email(email)
        with allure.step(f"Нажимаю кнопку {self.SUBMIT_BUTTON}"):
            self.find(locator=self.SUBMIT_BUTTON).click()
        self._set_passw(passw)
        with allure.step(f"Нажимаю кнопку {self.SUBMIT_BUTTON}"):
            self.find(locator=self.SUBMIT_BUTTON).click()
        # with allure.step(f"Пропуск предложения привязать телефон"):
        #     self.find(locator=self.SKIP_PHONE_BUTTON).click()

    def go_to_hd(self):
        with allure.step("Перехожу в онлайн кинотеатр"):
            self.find(locator=self.HD_LINK).click()
        with allure.step("Смотрю, что на странице есть вкладка 'Мои покупки'"):
            self.find(locator=self.MY_BUYS)

    def search_movie(self, movie_name):
        with allure.step(f"Ввожу в поиск фильм: {movie_name}"):
            self.find(locator=self.SEARCH_FIELD).send_keys(movie_name)
        with allure.step(f"Запускаю поиск фильма: {movie_name}"):
            self.find(locator=self.SEARCH_BUTTON).click()