import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title('Покупка тура с одобрением')
@allure.description('Проверяем, что при вводе данных карты APPROVED форма подтверждает покупку')
def test_ui_payment_approved():
    driver = webdriver.Chrome()
    try:
        with allure.step('Открытие страницы'):
            driver.get('http://localhost:8080')

        with allure.step('Заполнение формы покупки'):
            card_number = driver.find_element(By.NAME, 'cardNumber')
            card_number.send_keys('4444 4444 4444 4441')

            expiry = driver.find_element(By.NAME, 'expiry')
            expiry.send_keys('12/25')

            cvc = driver.find_element(By.NAME, 'cvc')
            cvc.send_keys('123')

        with allure.step('Отправка формы'):
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        with allure.step('Проверка результата'):
            success_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'success'))
            )
            assert 'успешно' in success_message.text

    finally:
        driver.quit()
