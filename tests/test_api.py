import requests
import allure

# Используем имя сервиса из docker-compose.yml / allure_report.yml
BASE_GATE_URL = "http://localhost:9999"

@allure.title("API: Покупка тура с APPROVED картой")
@allure.description("Отправляем данные карты 4444 4444 4444 4441, ожидаем APPROVED")
def test_payment_approved():
    payload = {"number": "4444 4444 4444 4441"}
    with allure.step("Отправка POST-запроса на /payment"):
        response = requests.post(f"{BASE_GATE_URL}/payment", json=payload)
    with allure.step("Проверка статуса 200"):
        assert response.status_code == 200
    with allure.step("Проверка ответа APPROVED"):
        assert response.json()["status"] == "APPROVED"

@allure.title("API: Покупка тура с DECLINED картой")
@allure.description("Отправляем данные карты 4444 4444 4444 4442, ожидаем DECLINED")
def test_payment_declined():
    payload = {"number": "4444 4444 4444 4442"}
    with allure.step("Отправка POST-запроса на /payment"):
        response = requests.post(f"{BASE_GATE_URL}/payment", json=payload)
    with allure.step("Проверка статуса 200"):
        assert response.status_code == 200
    with allure.step("Проверка ответа DECLINED"):
        assert response.json()["status"] == "DECLINED"