from locators.locators import PageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_desktops_page(browser):
    browser.get(browser.url + "/index.php?route=product/category&path=20")

    try:
        WebDriverWait(browser, 1).until(EC.presence_of_element_located(PageLocators.DESKTOPS))
    except TimeoutException:
        print('Страница не загружена')

    assert browser.find_element(*PageLocators.DESKTOPS), "Открыта некорректная страница"

    footer_blocks = browser.find_elements(*PageLocators.FOOTER)
    assert len(footer_blocks) == 4, "Неверное количество списков ссылок в футере"

    elements = browser.find_elements(*PageLocators.LIST_GROUP)
    assert len(elements) == 10, "Неверное количество элементов в списке"

    products = browser.find_elements(*PageLocators.PRODUCTS)
    assert len(products) == 12, "Неверное количество продуктов в списке"

    assert browser.find_element(*PageLocators.CART), 'Отсутствует корзина'
