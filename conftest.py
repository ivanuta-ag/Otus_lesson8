import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="https://demo.opencart.com/")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(executable_path="c:/selenium_drivers/chromedriver.exe", options=chrome_options)

    elif browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(executable_path="c:/selenium_drivers/geckodriver.exe", options=firefox_options)

    elif browser == "ie":
        driver = webdriver.Ie(executable_path="c:/selenium_drivers/IEDriverServer.exe")

    else:
        raise pytest.UsageError("--browser_name should be chrome, firefox or ie")

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
