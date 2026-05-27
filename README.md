# Автотесты для Stellar Burgers

Проект UI-автотестов для учебного сервиса **Stellar Burgers**.

## Стек
- Python
- Pytest
- Selenium WebDriver
- Requests
- Allure Pytest

## Что покрыто
- Главная страница и вкладки конструктора
- Модальное окно ингредиента
- Личный кабинет и история заказов
- Восстановление пароля
- Создание заказа
- Лента заказов

## Структура проекта
- `conftest.py` — фикстуры, инициализация драйвера, создание и удаление тестовых пользователей
- `urls.py` — ссылки на страницы и API
- `locators/` — локаторы страниц
- `pages/` — page object классы
- `tests/` — UI-тесты

## Установка зависимостей
```bash
pip install -r requirements.txt
```

## Запуск тестов
Запуск всех тестов:
```bash
python -m pytest -v
```

Запуск в Firefox:
```bash
python -m pytest -v --browser firefox
```

Запуск в Chrome:
```bash
python -m pytest -v --browser chrome
```

## Allure
Запуск тестов с генерацией результатов:
```bash
python -m pytest -v --alluredir=allure_results
```

Запуск тестов с Allure в Firefox:
```bash
python -m pytest -v --browser firefox --alluredir=allure_results
```

Запуск тестов с Allure в Chrome:
```bash
python -m pytest -v --browser chrome --alluredir=allure_results
```

Открыть отчёт:
```bash
allure serve allure_results
```

## Результат
Проект использует Page Object Model и покрывает основные пользовательские сценарии сервиса Stellar Burgers.