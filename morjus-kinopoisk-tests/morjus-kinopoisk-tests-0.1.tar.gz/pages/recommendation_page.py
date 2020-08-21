import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RecommendationPage(BasePage):
    RECOMMENDATION_HEADER = (By.XPATH, '//h1[contains(text(), "Рекомендации")]')
    ONLINE_TAB = (By.XPATH, '//span[contains(text(), "Онлайн")]')
    TOTAL_ONLINE_MOVIES = (By.XPATH, '//a/span[contains(text(), "фильмов")]')
    LINKS_FOR_MOVIES_PLUS = (By.XPATH, '//a[contains(text(), "По подписке Плюс")]')

    MOVIE_NAME = (By.CSS_SELECTOR, 'div div span img')


    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.base_url = url

    def switch_tab_to_online(self):
        with allure.step("Переключение на вкладку онлайн в рекомендациях"):
            self.find(locator=self.ONLINE_TAB).click()
            self.find(locator=self.TOTAL_ONLINE_MOVIES)

    def go_to_watch_online_random_movie_from_list(self):
        with allure.step("Ищу все ссылки на просмотр фильмов по плюс подписке"):
            movies = self.finds(locator=self.LINKS_FOR_MOVIES_PLUS)
        with allure.step("Выбираю случайный фильм для просмотра"):
            import random
            movie = random.choice(movies)
        with allure.step(f"Перехожу к просмотру"):
            movie.click()
        with allure.step("Проверяю, что открылся фильм"):
            element = self.find(locator=self.MOVIE_NAME)
            movie_name = element.get_attribute("alt")

        with allure.step(f"Открылся фильм: {movie_name}"):
            return movie_name
