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


@allure.feature("DB Tests")
@allure.story("Payment Entity Check")
def test_payment_entity_table_exists(db_connection):
    """
    Проверяет, что таблица payment_entity существует.
    """
    cursor = db_connection.cursor()
    # Запрос для получения списка таблиц
    cursor.execute("SHOW TABLES LIKE 'payment_entity';")
    result = cursor.fetchone()
    cursor.close()

    with allure.step("Проверка наличия таблицы payment_entity"):
        assert result is not None, "Таблица payment_entity не найдена в БД"


@allure.feature("DB Tests")
@allure.story("Credit Request Entity Check")
def test_credit_request_entity_table_exists(db_connection):
    """
    Проверяет, что таблица credit_request_entity существует.
    """
    cursor = db_connection.cursor()
    # Запрос для получения списка таблиц
    cursor.execute("SHOW TABLES LIKE 'credit_request_entity';")
    result = cursor.fetchone()
    cursor.close()

    with allure.step("Проверка наличия таблицы credit_request_entity"):
        assert result is not None, "Таблица credit_request_entity не найдена в БД"

# ... другие DB-тесты, если нужно ...