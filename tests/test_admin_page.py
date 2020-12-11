from locators.locators import PageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_desktops_page(browser):
    browser.get(browser.url + "/admin")
    try:
        WebDriverWait(browser, 1).until(EC.presence_of_element_located(PageLocators.LOGIN_TEXT))
    except TimeoutException:
        print('Страница не загружена')

    assert browser.find_element(*PageLocators.LOGIN_TEXT), "Некорректный текст с просьбой залогиниться"

    assert browser.find_element(*PageLocators.INPUT_USERNAME), "Отсутствует поле ввода логина"

    assert browser.find_element(*PageLocators.LOGIN), "Отсутствует поле E-Mail Address"

    assert browser.find_element(*PageLocators.INPUT_PASSWORD), "Отсутствует поле Password"

    assert browser.find_element(*PageLocators.HELP_BLOCK), "Отсутствует help-block"


def test_login_admin_page(browser):
    browser.get(browser.url + "/admin")
    browser.find_element(*PageLocators.LOGIN).click()

    assert browser.find_element(*PageLocators.USER_PROFILE), 'Пользователь не залогинен'

    browser.find_element(*PageLocators.LOGOUT).click()
    assert browser.find_element(*PageLocators.LOGIN_TEXT), "Не появился текст с просьбой залогиниться"


def test_table_with_goods(browser):
    browser.get(browser.url + "/admin")
    browser.find_element(*PageLocators.LOGIN).click()
    browser.find_element(*PageLocators.PARENT_COLLAPSE).click()
    browser.find_element(*PageLocators.PRODUCTS_CATALOG).click()

    assert browser.find_element(*PageLocators.TABLE_RESPONSITIVE), 'Пользователь не залогинен'
