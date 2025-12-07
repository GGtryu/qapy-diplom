import requests
import allure

# Используем имя сервиса из docker-compose.yml
BASE_GATE_URL = "http://gate-simulator:9999"

@allure.title("Проверка APPROVED карты")
@allure.description("Отправляем запрос с картой 4444 4444 4444 4441, ожидаем APPROVED")
def test_approved_payment():
    payload = {"number": "4444 4444 4444 4441"}

    with allure.step("Отправка POST-запроса на /payment"):
        response = requests.post(f"{BASE_GATE_URL}/payment", json=payload)

    with allure.step("Проверка статуса 200"):
        assert response.status_code == 200

    with allure.step("Проверка ответа APPROVED"):
        assert response.json()["status"] == "APPROVED"

@allure.title("Проверка APPROVED карты")
@allure.description("Отправляем запрос с картой 4444 4444 4444 4441, ожидаем APPROVED")
def test_approved_payment():
    payload = {"number": "4444 4444 4444 4441"}

    with allure.step("Отправка POST-запроса на /payment"):
        response = requests.post(f"{BASE_GATE_URL}/payment", json=payload)

    with allure.step("Проверка статуса 200"):
        assert response.status_code == 200

    with allure.step("Проверка ответа APPROVED"):
        assert response.json()["status"] == "APPROVED"

    # Добавим комментарий для принудительного изменения
    # Это гарантирует новый запуск GitHub Actions