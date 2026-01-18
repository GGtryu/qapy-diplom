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
    # Для CI или headless режима:
    # options.add_argument("--headless=new")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--window-size=1920,1080")

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
        # Эти параметры должны совпадать с настройками в docker-compose.yml и application.properties
        connection = mysql.connector.connect(
            host='localhost', # или '127.0.0.1'. Если контейнер БД запущен с другим именем в compose, используйте его.
            port=3307,        # <-- Используем внешний порт 3307, как в docker-compose.yml
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