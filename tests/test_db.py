import allure
import mysql.connector

# Используем имя сервиса из allure_report.yml
DB_CONFIG = {
    'host': 'mysql',
    'port': 3306,
    'user': 'app',
    'password': 'app',
    'database': 'app'
}

@allure.title("DB: Проверка подключения к БД")
@allure.description("Проверяем, что можно подключиться к базе данных")
def test_db_connection():
    with allure.step("Подключение к БД"):
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

    with allure.step("Выполнение простого запроса"):
        cursor.execute("SELECT 1;")

    with allure.step("Проверка результата"):
        result = cursor.fetchone()
        assert result[0] == 1

    cursor.close()
    connection.close()