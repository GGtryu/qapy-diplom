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
    options.add_argument("--disable-dev-shm-usage