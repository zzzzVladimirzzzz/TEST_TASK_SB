from selenium.webdriver.common.by import By


class LocatorsLoginPage:
    PASSWORD_ERROR_MESSAGE_RU = 'Неверный логин или пароль. Если не можете войти,'
    PASSWORD_ERROR_MESSAGE_CAPTCH = 'Мы просим ввести этот код для вашей безопасности, ' \
                                    'чтобы убедиться, что вы не программа для подбора паролей.'
    LOCATOR_LOGIN = (By.XPATH, "//*[contains(@data-testid, 'login-select-continue')]")
    LOCATOR_INPUT_LOGIN = (By.XPATH, "//*[contains(@name, 'login')]")
    LOCATOR_INPUT_PASSWORD = (By.XPATH, "//*[contains(@name, 'password')]")
    LOCATOR_BUTTON_CONTINUE = (By.XPATH, "//button[contains(@data-testid, 'button-continue')]")
    LOCATOR_PASSWORD_ERROR = (By.XPATH, "//button[contains(@id, 'password-error')]")
