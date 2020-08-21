import allure
from random import choice
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.header_page import HeaderPage


class MediaPage(HeaderPage):

    TESTS_PAGE = (By.XPATH, '//a[contains(text(), "Тесты")]')
    TESTS_HEADERS = (By.XPATH, '//span[contains(text(), "Тест")]')
    TEST_CARDS = (By.CSS_SELECTOR, "a[href^='/media/game'][href$='/']")

    TEST_HEADLINE = (By.CSS_SELECTOR, '[itemprop="headline"]')

    TEST_FRAME = (By.CSS_SELECTOR, '[id^="iframe"]')
    TOTAL_QUESTIONS = (By.CSS_SELECTOR, '.question-header__page')
    QUESTION = (By.CSS_SELECTOR, "h2.question-header__title")
    ANSWER_ITEMS = (By.CSS_SELECTOR, '.answers-item')
    NEXT_QUESTION_BUTTON = (By.CSS_SELECTOR, ".next-question-button")
    QUIZ_RESULT = (By.CSS_SELECTOR, ".result-image")

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.base_url = url

    def go_to_tests_tab(self):
        numbers_of_headers = 20
        with allure.step("Выбор вкладки с тестами"):
            self.find(locator=self.TESTS_PAGE).click()
        with allure.step("Ищу все заголовками с названием Тест внутри них"):
            list_of_headers = self.finds(locator=self.TESTS_HEADERS)
        with allure.step(f"Проверяю общее количества заголовков, должно быть больше {numbers_of_headers}"):
            assert len(list_of_headers) > numbers_of_headers, f"Слишком мало заголовков, найдено {list_of_headers}"

    def choice_random_test(self):
        with allure.step("Ищу все карточки с тестами"):
            list_of_tests = self.finds(locator=self.TEST_CARDS)[1:]
        with allure.step("Выбираю случайную карточку с тестом"):
            import random
            random.choice(list_of_tests).click()

            test_name = self.find(locator=self.TEST_HEADLINE).text
        with allure.step(f"Выбран тест под названием{test_name}"):
            return test_name

    def pass_test(self):
        with allure.step("Переключаюсь на окошко с тестом"):
            frame = self.find(locator=self.TEST_FRAME, time=10)
            self.driver.switch_to.frame(frame)
        with allure.step("Считаю общее количество вопросов"):
            count_questions = self.find(locator=self.TOTAL_QUESTIONS).text
            count_questions = count_questions.split(" ")
            total_questions = int(count_questions.pop().strip())
        with allure.step(f"Общее количество вопросов {total_questions}, случайно отвечаю на вопросы в цикле"):

            for _ in range(total_questions):
                question = self.find(locator=self.QUESTION).text
                with allure.step(f"Отвечаю на вопрос теста {question}"):
                    with allure.step(f"Выбираю случайный ответ"):
                        answers = self.finds(locator=self.ANSWER_ITEMS)
                        answer = choice(answers)
                    with allure.step(f"Выбран ответ {answer.text}"):
                        answer.click()
                try:
                    with allure.step(f"Переход к следующему вопросу"):
                        self.find(locator=self.NEXT_QUESTION_BUTTON, time=1).click()
                except TimeoutException:
                    pass

            try:
                with allure.step(f"Выбираю случайный ответ"):
                    answers = self.finds(locator=self.ANSWER_ITEMS, time=2)
                    answer = choice(answers)
                with allure.step(f"Выбран ответ {answer.text}"):
                    answer.click()
                with allure.step(f"Переход к последнему вопросу"):
                    self.find(locator=self.NEXT_QUESTION_BUTTON, time=1).click()
            except TimeoutException:
                pass

            with allure.step("Беру текст из картинки с результатом теста"):
                quiz_result_title = self.find(locator=self.QUIZ_RESULT)
                result_title = quiz_result_title.get_attribute('alt')
            with allure.step(f"Результат теста: {result_title}"):
                return result_title

