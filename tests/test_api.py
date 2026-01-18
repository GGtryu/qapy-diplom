# tests/test_api.py
import requests
import pytest
import allure

# --- Конфигурация ---
# URL для API-тестов (должен соответствовать адресу gate-simulator в GitHub Actions)
BASE_GATE_URL = "http://localhost:9999" # <-- Используем localhost:9999, как настроено в workflow

# --- Тесты ---
@allure.feature("API Tests")
@allure.story("Payment Processing")
def test_payment_approved():
    """
    Отправляем данные карты 4444 4444 4444 4441, ожидаем APPROVED.
    """
    payload = {"number": "4444 4444 4444 4441"}
    with allure.step(f"Отправка POST-запроса на /api/v1/process-payment с payload: {payload}"):
        response = requests.post(f"{BASE_GATE_URL}/api/v1/process-payment", json=payload) # Убедимся, что путь правильный
    with allure.step(f"Проверка статуса 200. Ответ: {response.status_code}, {response.text}"):
        assert response.status_code == 200, f"Ожидаемый статус 200, получен {response.status_code}. Ответ: {response.text}"
    with allure.step("Проверка тела ответа на наличие 'APPROVED'"):
        response_data = response.json()
        # Пример:
        # assert response_data.get("status") == "APPROVED", f"Ожидаемый статус APPROVED, получен {response_data.get('status')}"
        # Или:
        assert response_data.get("result") == "APPROVED", f"Ожидаемый результат APPROVED, получен {response_data.get('result')}"


@allure.feature("API Tests")
@allure.story("Payment Processing")
def test_payment_declined():
    """
    Отправляем данные карты 4444 4444 4444 4442, ожидаем DECLINED.
    """
    payload = {"number": "4444 4444 4444 4442"}
    with allure.step(f"Отправка POST-запроса на /api/v1/process-payment с payload: {payload}"):
        response = requests.post(f"{BASE_GATE_URL}/api/v1/process-payment", json=payload)
    with allure.step(f"Проверка статуса 200. Ответ: {response.status_code}, {response.text}"):
        assert response.status_code == 200, f"Ожидаемый статус 200, получен {response.status_code}. Ответ: {response.text}"
    with allure.step("Проверка тела ответа на наличие 'DECLINED'"):
        response_data = response.json()
        # Пример:
        # assert response_data.get("status") == "DECLINED", f"Ожидаемый статус DECLINED, получен {response_data.get('status')}"
        # Или:
        assert response_data.get("result") == "DECLINED", f"Ожидаемый результат DECLINED, получен {response_data.get('result')}"

# ... другие API-тесты, если нужно ...