import allure

@allure.title("Заглушка UI-теста")
@allure.description("Проверка UI-теста отключена")
def test_ui_payment_approved():
    with allure.step("Тест отключен"):
        pass