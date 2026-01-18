# tests/conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import mysql.connector
import time
import subprocess
import os

# --- Фикстура для Selenium WebDriver ---
@pytest.fixture(scope="function")  # scope="function" означает, что драйвер создается для каждого теста
def driver():
    # Убедитесь, что ChromeDriver доступен. webdriver_manager автоматически скачает его.
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # --- Добавленные опции для CI/CD ---
    options.add_argument("--headless=new") # Запуск в headless режиме
    options.add_argument("--no-sandbox") # Отключение sandbox (часто требуется в CI)
    options.add_argument("--disable-dev-shm-usage") # <-- Исправлено: добавлена закрывающая кавычка
    options.add_argument("--disable-gpu") # Отключение GPU (опционально, но безопасно)
    options.add_argument("--window-size=1920,1080") # Установка размера окна (для headless)
    # --- Конец добавленных опций ---

    # Для локального запуска с открытием окна браузера:
    # options.add_experimental_option("detach", True) # Опционально: оставляет браузер открытым после теста

    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)  # Ждём до 10 секунд при поиске элементов
    yield driver
    driver.quit()

# --- Фикстура для подключения к БД ---
@pytest.fixture(scope="function") # scope="function", если нужно, чтобы соединение открывалось/закрывалось для каждого теста
def db_connection():
    connection = None
    try:
        # Эти параметры должны соответствовать настройкам, используемым в docker-compose.yml
        # host и port должны указывать на сервис MySQL, запущенный в Docker, и мапящийся на хост (runner)
        # Если в docker-compose.yml указано ports: - "3307:3306", то порт на хосте (runner) - 3307
        connection = mysql.connector.connect(
            host='localhost', # <-- Используем localhost, как адрес на runner
            port=3307,        # <-- Используем порт 3307, как мапится в docker-compose.yml (внешний порт)
            user='app',       # Пользователь из application.properties
            password='pass',  # Пароль из application.properties
            database='app'    # Название БД из application.properties
        )
        yield connection
    except mysql.connector.Error as err:
        print(f"Ошибка подключения к БД: {err}")
        pytest.fail(f"Не удалось подключиться к БД: {err}")
    finally:
        if connection and connection.is_connected():
            connection.close()
