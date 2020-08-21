import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HdPage(BasePage):

    MOVIE_NAME = (By.CSS_SELECTOR, 'div div span img')
    AVATAR_MENU = (By.CSS_SELECTOR, "button[class^='ProfileMenu']")
    CREATE_CHILD_PROFILE_LINK = (By.CSS_SELECTOR, "ul[class^='ProfileMenu'] a[href^='/create-profiles']")
    CREATE_CHILD_HEADER = (By.XPATH, '//div/h1[contains(text(), "Как зовут ребенка?")]')

    PROMO = (By.CSS_SELECTOR, "div div a[href^='/special']")
    BUTTONS_ON_PROMO_PAGE = (By.CSS_SELECTOR, "section[class^='Landing'] button")

    CHILD_NAME = (By.CSS_SELECTOR, '#name')
    NEXT_BUTTON = (By.XPATH, '//button/span[contains(text(), "Далее")]')

    PAY_IFRAME = (By.CSS_SELECTOR, 'body[cz-shortcut-listen="true"]')
    PAY_HEADER = (By.XPATH, "//div/span/h1")

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.base_url = url

    def get_name_of_opened_movie(self):
        with allure.step("Проверяю, что открылся фильм"):
            element = self.find(locator=self.MOVIE_NAME)
            movie_name = element.get_attribute("alt")

        with allure.step(f"Открылся фильм: {movie_name}"):
            return movie_name

    def go_to_create_child_profile(self):
        with allure.step("Открываю меню профиля через аватар"):
            self.find(locator=self.AVATAR_MENU).click()
        with allure.step("Переход к созданию детского профиля"):
            self.find(locator=self.CREATE_CHILD_PROFILE_LINK).click()
        with allure.step("Смотрю, что заголовок спрашивает 'Как зовут ребенка?'"):
            self.find(locator=self.CREATE_CHILD_HEADER)

    def go_to_promo_page(self):
        with allure.step("Открываю ссылку 'Спецпредложение'"):
            self.find(locator=self.PROMO).click()
        with allure.step("Перехожу к получению промокода"):
            with allure.step("Переключаюсь на активную вкладку"):
                self.driver.switch_to.window(self.driver.window_handles[1])

    def pay_for_access(self):
        with allure.step("Нажимаю на кнопку оформления"):
            self.finds(locator=self.BUTTONS_ON_PROMO_PAGE)[0].click()
        with allure.step("Беру заголовок в окошке оплаты"):
            return self.find(locator=self.PAY_HEADER).text


