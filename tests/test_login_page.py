from locators.locators import PageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_desktops_page(browser):
    browser.get(browser.url + "/index.php?route=account/login")
    try:
        WebDriverWait(browser, 1).until(EC.presence_of_element_located(PageLocators.LOGIN_PAGE))
    except TimeoutException:
        print('Страница не загружена')

    assert browser.find_element(*PageLocators.LOGIN_PAGE), "Открыта некорректная страница"

    assert browser.find_element(*PageLocators.LOGIN_BUTTON), "Отсутствует кнопка логина"

    assert browser.find_element(*PageLocators.INPUT_EMAIL), "Отсутствует поле E-Mail Address"

    assert browser.find_element(*PageLocators.INPUT_PASSWORD), "Отсутствует поле Password"

    assert browser.find_element(*PageLocators.CONTINUE), "Отсутствует кнопка Continue"
