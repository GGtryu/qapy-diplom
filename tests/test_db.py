import allure
import mysql.connector

# Убедитесь, что используете имя сервиса из allure_report.yml
DB_CONFIG = {
    'host': 'mysql',  # или 'localhost', если запускаете локально
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

@allure.title("DB: Проверка существования таблицы")
@allure.description("Проверяем, что таблица users существует")
def test_table_exists():
    with allure.step("Подключение к БД"):
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

    with allure.step("Проверка, что таблица users существует"):
        cursor.execute("SHOW TABLES LIKE 'users';")
        result = cursor.fetchone()
        assert result is not None, "Таблица 'users' не найдена"

    cursor.close()
    connection.close()