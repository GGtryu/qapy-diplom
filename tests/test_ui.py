import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Используем имя сервиса из allure_report.yml, если запускаем в CI
BASE_UI_URL = "http://aqa-shop:8080"  # или "http://localhost:8080", если локально

@allure.title("UI: Проверка загрузки страницы")
@allure.description("Проверяем, что главная страница загружается")
def test_page_loads():
    options = Options()
    options.add_argument("--headless")  # Для запуска в CI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    try:
        with allure.step("Открытие главной страницы"):
            driver.get(BASE_UI_URL)
        with allure.step("Проверка заголовка"):
            assert "тур" in driver.title.lower()  # или другое ожидаемое слово
    finally:
        driver.quit()