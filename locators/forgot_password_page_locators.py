from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    email_input = (
        By.XPATH,
        "//input[@type='text' and @name='name'] | //input[@type='email']"
    )

    restore_button = (
        By.XPATH,
        "//button[contains(normalize-space(), 'Восстановить')]"
    )

    password_input = (
        By.XPATH,
        "//input[@type='password' or @type='text']"
    )

    password_eye_button = (
        By.XPATH,
        "//div[contains(@class, 'input__container')]//*[name()='svg' or contains(@class, 'input__icon')]"
    )

    reset_password_title = (
        By.XPATH,
        "//*[contains(normalize-space(), 'Восстановление пароля')]"
    )