from selenium.webdriver.common.by import By


class LoginPageLocators:
    email_input = (
        By.XPATH,
        "//input[@name='name' and @type='text']"
    )

    password_input = (
        By.XPATH,
        "//input[@name='Пароль' and @type='password']"
    )

    login_button = (
        By.XPATH,
        "//button[contains(normalize-space(), 'Войти')]"
    )

    forgot_password_link = (
        By.XPATH,
        "//a[contains(@href, 'forgot-password')]"
    )

    error_text = (
        By.XPATH,
        "//*[contains(text(), 'Некорректный') or contains(text(), 'невер') or contains(text(), 'Ошибка') or contains(text(), 'неуспеш')]"
    )