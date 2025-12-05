import allure
import mysql.connector

DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'app',
    'password': 'app',
    'database': 'app'
}

@allure.title('Проверка записи в БД')
@allure.description('Проверяем, что транзакция записывается в таблицу после покупки')
def test_db_transaction_recorded():
    with allure.step('Подключение к БД'):
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

    with allure.step('Запрос последней транзакции'):
        cursor.execute('SELECT status FROM transactions ORDER BY id DESC LIMIT 1;')
        result = cursor.fetchone()

    with allure.step('Проверка статуса транзакции'):
        assert result[0] in ['APPROVED', 'DECLINED']

    cursor.close()
    connection.close()
