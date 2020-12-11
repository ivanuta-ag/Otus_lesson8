from locators.locators import PageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_opencart_page(browser):
    assert browser.current_url == browser.url


def test_main_page(browser):
    browser.get(browser.url + "/index.php?route=account/login")

    try:
        WebDriverWait(browser, 1).until(EC.presence_of_element_located(PageLocators.HEART))
    except TimeoutException:
        print('Страница не загружена')

    assert browser.find_element(*PageLocators.HEART), 'Отсутствует wish list'

    menu_items = browser.find_elements(*PageLocators.NAVBAR_1)
    assert len(menu_items) == 8, 'Неверное количество элементов меню'

    assert browser.find_element(*PageLocators.NAVBAR_2), 'Отсутствует navbar'

    assert browser.find_element(*PageLocators.LOGO), 'Отсутствует logo'

    assert browser.find_element(*PageLocators.CART), 'Отсутствует корзина'
