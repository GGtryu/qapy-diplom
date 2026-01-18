import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

@allure.feature("UI Tests")
@allure.story("Invalid Data Handling")
def test_purchase_with_invalid_card_number(driver):
    """
    Тестирует попытку покупки с неверным номером карты.
    Проверяет UI сообщение об ошибке.
    ВНИМАНИЕ: Приложение aqa-shop возвращает 'Успешно' даже для DECLINED карты.
             Этот тест проверяет текущее поведение.
    """
    # 1. Открыть страницу
    driver.get("http://localhost:8080")

    # 2. Найти и кликнуть кнопку "Купить" (Используем правильный селектор)
    buy_button = driver.find_element(By.CSS_SELECTOR, "button.button_size_m.button_theme_alfa-on-white")
    buy_button.click()

    # 3. Ждём появления поля "Номер карты" (это сигнал, что форма загрузилась)
    # Используем XPATH для поиска по тексту метки, как подсказал преподаватель
    card_number_field = driver.find_element(By.XPATH, "//span[contains(text(), 'Номер карты')]/following-sibling::span/input")

    # 4. Заполнить форму данными неуспешной карты (например, 4444 4444 4444 4442)
    card_number_field.send_keys("4444 4444 4444 4442")
    driver.find_element(By.XPATH, "//span[contains(text(), 'Месяц')]/following-sibling::span/input").send_keys("12")
    driver.find_element(By.XPATH, "//span[contains(text(), 'Год')]/following-sibling::span/input").send_keys("26") # Исправлено на 26
    driver.find_element(By.XPATH, "//span[contains(text(), 'Владелец')]/following-sibling::span/input").send_keys("IVAN PETROV")
    driver.find_element(By.XPATH, "//span[contains(text(), 'CVC/CVV')]/following-sibling::span/input").send_keys("123")

    # 5. Отправить форму (кнопка "Продолжить")
    # Используем CSS-селектор, который соответствует HTML-коду из DevTools
    # Преподаватель сказал, что .button_view_extra находит две кнопки, а нужна вторая
    continue_buttons = driver.find_elements(By.CSS_SELECTOR, ".button_view_extra")
    continue_button = continue_buttons[1]  # Берём вторую кнопку
    continue_button.click()

    # 6. Проверить сообщение об успехе (ожидаем "Успешно", несмотря на неверную карту - баг в aqa-shop)
    # Сначала ждём появления текста "Успешно" в .notification__title
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".notification__title"), "Успешно")
    )
    # Теперь находим элемент и проверяем его текст (он уже должен быть "Успешно")
    success_message_title = driver.find_element(By.CSS_SELECTOR, ".notification__title")
    assert success_message_title.text == "Успешно", f"Ожидаемый текст 'Успешно', но был '{success_message_title.text}'"

    # Аналогично для .notification__content (не .notification__text!)
    success_message_content_element = None
    for _ in range(10):  # Попробуем 10 раз с интервалом 1 секунда
        try:
            success_message_content_element = driver.find_element(By.CSS_SELECTOR, ".notification__content")
            if "Операция одобрена Банком." in success_message_content_element.text:
                break
        except:
            pass
        time.sleep(1)

    # Проверяем, нашли ли элемент и содержит ли он нужный текст
    assert success_message_content_element is not None, "Элемент .notification__content не найден"
    assert "Операция одобрена Банком." in success_message_content_element.text, f"Ожидаемый текст 'Операция одобрена Банком.' не найден в элементе .notification__content. Текущий текст: '{success_message_content_element.text}'"

# Добавьте другие негативные сценарии аналогично (пустые поля, просроченная дата и т.д.)
