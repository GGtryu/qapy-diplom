# qapy-diplom

Дипломный проект по автоматизации тестирования.

## Требования

- Docker
- Docker Compose
- Python 3.8+
- Git
- Node.js (для запуска `gate-simulator` вручную, если не через `docker-compose`)

## Установка и запуск

1.  **Клонируйте репозиторий:**

    ```bash
    git clone <YOUR_REPOSITORY_URL>
    cd <YOUR_REPOSITORY_NAME>
    ```

2.  **Важно:** Убедитесь, что у вас есть файл `aqa-shop.jar` в корне папки проекта. Если его нет, получите его из материалов курса.

3.  **Запустите приложение и его зависимости (MySQL, gate-simulator) с помощью Docker Compose:**

    ```bash
    docker-compose up --build -d
    ```

    Подождите **30-60 секунд**, чтобы все сервисы (особенно `aqa-shop`) полностью запустились. Проверить статус можно командой `docker-compose ps`.

4.  **Создайте и активируйте виртуальное окружение Python:**

    ```bash
    python -m venv venv
    # Для Windows PowerShell:
    venv\Scripts\activate
    # Для Linux/macOS или Git Bash:
    # source venv/bin/activate
    ```

5.  **Установите зависимости:**

    ```bash
    pip install -r requirements.txt
    ```

6.  **Запустите UI-тесты:**

    ```bash
    pytest tests/ui_tests/ --alluredir=./allure-results -v
    ```

7.  **(Опционально) Для просмотра отчёта Allure в браузере (требуется установленный Allure CLI):**

    ```bash
    allure serve ./allure-results
    ```

## Структура проекта

- `docker-compose.yml` - Конфигурация для запуска приложения, MySQL и gate-simulator.
- `application.properties` - Конфигурация приложения.
- `aqa-shop.jar` - Исполняемый JAR-файл основного приложения.
- `gate-simulator/` - Код эмулятора платежного шлюза.
- `tests/` - Каталог с тестами.
- `conftest.py` - Фикстуры для pytest.
- `ui_tests/` - UI-тесты.
