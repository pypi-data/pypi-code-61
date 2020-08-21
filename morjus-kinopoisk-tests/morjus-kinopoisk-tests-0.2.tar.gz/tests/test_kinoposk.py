import pytest
import allure
from pages.header_page import HeaderPage
from pages.main_page import MainPage
from pages.movie_page import MoviePage
from pages.user_page import UserPage
from pages.recommendation_page import RecommendationPage
from pages.hd_profiles_page import HdProfilesPage
from pages.hd_page import HdPage
from pages.search_page import SearchPage
from pages.media_page import MediaPage
import os
from dotenv import load_dotenv

load_dotenv()


@allure.epic("Возможности авторизованного юзера")
@allure.feature("Авторизация")
@allure.story("Авторизация с валидными данными")
@pytest.mark.parametrize('auth', [
    (os.getenv("LOGIN"), os.getenv("PASSWORD"))
])
def test_login(browser, auth):
    page = HeaderPage(browser, url="https://www.kinopoisk.ru/")
    page.open()
    page.login(*auth)

    main_page = MainPage(page.driver, page.driver.current_url)
    header = main_page.check_main_header()
    assert header == "Главное сегодня", f"Заголовок 'Главное сегодня' не найден. Найдено: {header}"


@allure.epic("Возможности авторизованного юзера")
@allure.feature("Рейтинг фильма")
@allure.story("Выставление оценки фильму авторизованного пользователя и удаление оценки")
@pytest.mark.parametrize("rating", [10])
def test_set_rating(browser, rating):
    page = MoviePage(browser, url="https://www.kinopoisk.ru/film/693969/")
    page.open()
    page.login(os.getenv("LOGIN"), os.getenv("PASSWORD"))

    page.set_rating(rating)
    result_rating = page.check_rating_on_page()
    assert int(result_rating) == rating, f"Оценка на странице: {result_rating} не соответствует ожидаемой {rating}"

    page.delete_rating_on_page()
    assert page.check_rating_is_not_presented() is True, "Оценка фильма не удалена"


@allure.epic("Возможности авторизованного юзера")
@allure.feature("Папки с фильмами юзера")
@allure.story("Добавление фильма в папку 'Смотреть позже' и его удаление")
@pytest.mark.parametrize('auth', [
    (os.getenv("LOGIN"), os.getenv("PASSWORD"))
])
def test_add_to_watch_later(browser, auth):
    movie_page = MoviePage(browser, url="https://www.kinopoisk.ru/film/693969/")
    movie_page.open()
    movie_page.login(*auth)

    movie_page.add_to_watch_later()
    movie_name = movie_page.get_movie_name()
    movie_page.go_to_watch_later_list()
    user_page = UserPage(movie_page.driver, movie_page.driver.current_url)
    name = user_page.get_first_movie_in_watch_later_list()
    assert movie_name == name, f"Имена {movie_name} на странице фильма и {name} в списке 'Буду смотреть' не совпадают"

    result = user_page.del_first_from_watch_later()
    assert result is True, f"Фильм из списка не удален"


@allure.epic("Возможности авторизованного юзера")
@allure.feature("Смотреть онлайн на кинопоиск HD")
@allure.story("Переход из рекомендаций сразу к просмотру фильма онлайн по плюс подписке")
def test_from_recommends_go_to_online(browser):
    main_page = MainPage(browser, url="https://www.kinopoisk.ru/")
    main_page.open()
    main_page.login(os.getenv("LOGIN"), os.getenv("PASSWORD"))
    main_page.go_to_recommendations()

    recom_page = RecommendationPage(main_page.driver, main_page.driver.current_url)
    recom_page.switch_tab_to_online()
    recom_page.go_to_watch_online_random_movie_from_list()

    hd_page = HdPage(recom_page.driver, recom_page.driver.current_url)
    movie_name = hd_page.get_name_of_opened_movie()
    assert movie_name is not None, f"Названия фильма на странице нет, есть {movie_name}"


@allure.epic("Возможности авторизованного юзера")
@allure.feature("Детский профиль")
@allure.story("Создание детского профиля")
def test_create_child_profile(browser):
    main_page = MainPage(browser, url="https://www.kinopoisk.ru/")
    main_page.open()
    main_page.login(os.getenv("LOGIN"), os.getenv("PASSWORD"))

    main_page.go_to_hd()
    hd_page = HdPage(main_page.driver, main_page.driver.current_url)
    hd_page.go_to_create_child_profile()

    create_profile_page = HdProfilesPage(hd_page.driver, hd_page.driver.current_url)
    final_header = create_profile_page.create_child_profile("Зайка")
    assert final_header == 'Волшебный мир мультфильмов скрыт за подпиской', f"Заголовок найден, но иной:{final_header}"
    # should add method for removing profile


@allure.epic("Акции для юзеров")
@allure.feature("Промокод")
@allure.story("Проверка использования промокода")
def test_promocode(browser):
    main_page = MainPage(browser, url="https://www.kinopoisk.ru/")
    main_page.open()
    main_page.login(os.getenv("LOGIN"), os.getenv("PASSWORD"))

    main_page.go_to_hd()
    hd_page = HdPage(main_page.driver, main_page.driver.current_url)
    hd_page.go_to_promo_page()

    header = hd_page.pay_for_access()
    assert header == "Подписка Плюс Мульти с Амедиатекой", f"Заголовок найден, но иной:{header}"


@allure.epic("Поиск")
@allure.feature("Поисковая строка")
@allure.story("Правильное название фильма в поиске ведет к результатам, где введенный в поиск фильм на первом месте")
@pytest.mark.parametrize("movie_to_search", ["Аватар"])
def test_search(browser, movie_to_search):
    movie_to_search = "Аватар"

    main_page = MainPage(browser, url="https://www.kinopoisk.ru/")
    main_page.open()
    main_page.search_movie(movie_to_search)

    search_page = SearchPage(main_page.driver, main_page.driver.current_url)
    found_movie = search_page.check_guessing_of_search()
    assert found_movie == movie_to_search, f"Попытка угадать неверная, предложен {found_movie}"


@allure.epic("Статьи")
@allure.feature("Тесты")
@allure.story("Прохождение теста в статье приводит к результу")
def test_pass_quiz(browser):
    media_page = MediaPage(browser, url="https://www.kinopoisk.ru/media/")
    media_page.open()

    media_page.go_to_tests_tab()
    media_page.choice_random_test()

    result = media_page.pass_test()
    assert isinstance(result, str), f"Результат квиза не найден. Получено: {result}"


@allure.epic("Кинотеатры")
@allure.feature("Покупка билетов")
@allure.story("Покупка билетов в кинотеатр с главной страницы")
def test_buy_tickets_from_main_page(browser):
    main_page = MainPage(browser, url="https://www.kinopoisk.ru/")
    main_page.open()
    # Карусель с фильмами в кинотеатрах появляется не всегда
    main_page.select_random_movie_from_today_in_cinema()
    movie_in_pay_frame = main_page.buy_random_tickets()
    assert main_page.movie_to_go == movie_in_pay_frame, f"Название фильма в виджете оплаты не совпадает с названием " \
                                                        f"на главной, получено {movie_in_pay_frame}"


@allure.epic("Страница фильма")
@allure.feature("Трейлеры")
@allure.story("Присутствие трейлера на любой странце")
@pytest.mark.parametrize("movie_to_search", ["Аватар"])
def test_trailers(browser, movie_to_search):
    search_page = SearchPage(browser, url="https://www.kinopoisk.ru/")
    search_page.open()
    search_page.search_movie(movie_to_search)

    search_page.check_guessing_of_search()
    search_page.go_to_guessing_movie()

    movie_page = MoviePage(search_page.driver, search_page.driver.current_url)
    movie_name = movie_page.get_movie_name()
    name_in_iframe = movie_page.open_trailer()
    assert movie_name == name_in_iframe, f"Имя фильма в открывшемся трейлере не совпадает со страницей"
