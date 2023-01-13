import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from UI.pages.login_page import LoginPage


@pytest.fixture()
def driver(request):
    url = 'https://online.sberbank.ru/CSAFront/index.do'
    options = Options()
    if request.config.option.headless:
        options.add_argument('--headless')
        options.add_argument('--window-size=1280x1696')
        options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    driver.get(url)

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver=driver)
