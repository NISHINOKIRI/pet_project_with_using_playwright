import logging
import os
from colorama import Fore, Style


class Logger:

    def __init__(self, name):
        # Создаем директорию для логов, если она не существует
        self.log_directory = 'logs' # Задаём имя директории
        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)

        # Настройка имени файла для логов
        self.log_file = os.path.join(self.log_directory, f"{name}.log")

        # Создание логгера
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        # Создаем обработчик для записи логов в файл с кодировкой UTF-8
        file_handler = logging.FileHandler(self.log_file, encoding='utf-8')
        file_handler.setLevel(logging.INFO)

        # Создание форматировщика
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Добавление обработчика к логгеру
        self.logger.addHandler(file_handler)

        # Добавление StreamHandler для вывода логов в консоль
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(self.ConsoleFormatter())
        self.logger.addHandler(console_handler)

    class ConsoleFormatter(logging.Formatter):
        """Да-да, тут класс в классе, и да в него падает то что обрабатывается в логгере,
        всё окей, так работает так что пока что такая реализация"""
        def format(self, record):
            # Кастомизация вывода в консоль с цветами
            if record.levelno == logging.INFO:
                record.msg = f"{Fore.BLUE}{record.msg}{Style.RESET_ALL}"
            elif record.levelno == logging.WARNING:
                record.msg = f"{Fore.LIGHTGREEN_EX}{record.msg}{Style.RESET_ALL}"
            elif record.levelno == logging.ERROR:
                record.msg = f"{Fore.LIGHTYELLOW_EX}{record.msg}{Style.RESET_ALL}"
            elif record.levelno == logging.CRITICAL:
                record.msg = f"{Fore.RED}{Style.BRIGHT}{record.msg}{Style.RESET_ALL}"
            return super().format(record)

    def get_logger(self):
        return self.logger

# Пример использования см. 63 строку или просто запустить сам файл для теста

# Лог-тест:
# 1 - должна создаться папка в корне, т.е. в utils в данном случае
# 2 - должен создаться файл с именем "Losg's test"
# 3 - в файле должны появиться логи с теми типами которые прописаны ниже

if __name__ == "__main__":
    logger = Logger("Losg's test").get_logger()
    logger.info("Это информационное сообщение.")
    logger.warning("Это предупреждающее сообщение.")
    logger.error("Это сообщение об ошибке.")
    logger.critical("Это критическое сообщение.")