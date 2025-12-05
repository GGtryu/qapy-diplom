# Дипломный проект: qapy-diplom

## Описание
Автоматизация тестирования комплексного сервиса, взаимодействующего с СУБД и API платёжной системы.

## Стек
- Python 3
- pytest
- Selenium
- Allure
- MySQL
- Docker

## Запуск

1. Запустите сервисы:
   docker-compose up --build -d

2. Установите зависимости:
   pip install -r requirements.txt

3. Запустите тесты:
   pytest tests/ --alluredir=allure-results

4. Сгенерируйте отчёт:
   llure serve allure-results

## Отчёты
- [Plan.md](Plan.md) — план автоматизации
- [Report.md](Report.md) — результаты тестов
- [Summary.md](Summary.md) — итоги автоматизации
