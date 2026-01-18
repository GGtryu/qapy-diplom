# tests/test_db.py
import allure
import pytest
import mysql.connector
# Импортируем фикстуру db_connection из conftest.py
from tests.conftest import db_connection

@allure.feature("DB Tests")
@allure.story("DB Connection and Queries")
def test_db_connection(db_connection): # Используем фикстуру из conftest.py
    """
    Проверяет, что можно подключиться к базе данных.
    """
    with allure.step("Проверка подключения к БД"):
        assert db_connection.is_connected(), "Подключение к БД не установлено"

    # Пример выполнения простого запроса
    cursor = db_connection.cursor()
    with allure.step("Выполнение простого SELECT запроса"):
        cursor.execute("SELECT 1;")
        result = cursor.fetchone()
    with allure.step(f"Проверка результата запроса: {result}"):
        assert result is not None, "Запрос к БД не вернул результат"
        assert result[0] == 1, f"Ожидаемый результат 1, получен {result[0]}"
    cursor.close()

# ... другие DB-тесты, если нужно ...