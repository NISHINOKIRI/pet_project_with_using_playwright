import time
import pytest
from playwright.sync_api import sync_playwright, expect
from google_page.elems import Elems
from utils.loger import * # Импортируем функцию настройки логгера


link = str('https://www.google.com')

class Tests:
    # Инициализируем логгер
    logger = Logger('tests_log').get_logger()
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        # Инициализация Playwright и браузера
        self.playwright = sync_playwright().start()  # Запускаем Playwright
        self.browser = self.playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        yield  # Возвращаем управление тесту
        # Закрытие контекста и браузера после теста
        self.context.close()
        self.browser.close()
        self.playwright.stop()  # Остановка Playwright

    def test_pictures(self):
        print("\n")
        self.logger.warning("Начинаем тест")
        self.page.goto(link)
        self.logger.info(f"Открываем станицу {link}")
        # Клик на вкладку "Картинки"
        self.page.get_by_label(text='Поиск картинок').click()
        self.logger.info("Кликаем на элемент для поиска картинок")
        # Ожидание загрузки страницы
        self.page.wait_for_selector(Elems.pictures_lettering())
        self.logger.info("Ожидаем загрузку элемента")
        # Проверка текста на странице
        time.sleep(1)
        assert "Картинки" in self.page.inner_text(Elems.pictures_lettering()), self.logger.error("Элемент не найден") + self.logger.fatal("Тест провален\n")
        self.logger.info("Элемент загрузился")
        self.logger.warning("Тест пройден\n")

    def test_mail(self):
        print("\n")
        self.logger.warning("Начинаем тест")
        self.page.goto(link)
        self.logger.info(f"Открываем станицу {link}")
        # Ожидание загрузки элемента на странице
        self.page.wait_for_selector(Elems.mail_link())
        # Кликаем на ссылку
        self.page.get_by_label(text='Почта').click()
        self.logger.info("Кликаем на элемент для перехода на страницу почты")
        self.logger.info("Ожидаем загрузку элемента")
        # Проверка текста на странице
        time.sleep(1)
        assert "Gmail" in self.page.inner_text(Elems.mail_logo()), self.logger.error("Элемент не найден") + self.logger.fatal("Тест провален\n")
        self.logger.info("Элемент загрузился")
        self.logger.warning("Тест пройден\n")