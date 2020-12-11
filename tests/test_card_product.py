from locators.locators import PageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_desktops_page(browser):
    browser.get(browser.url + "/index.php?route=product/product&path=57&product_id=49")

    try:
        WebDriverWait(browser, 1).until(EC.presence_of_element_located(PageLocators.CARD_PRODUCT))
    except TimeoutException:
        print('Страница не загружена')

    assert browser.find_element(*PageLocators.CARD_PRODUCT), "Открыта некорректная страница"

    assert browser.find_element(*PageLocators.PRODUCT_IMAGE), "Отсутствует изображение товара"

    assert browser.find_element(*PageLocators.INPUT_QUANTITY), "Отсутствует форма добавления количества товаров"

    assert browser.find_element(*PageLocators.CART), 'Отсутствует корзина'

    assert browser.find_element(*PageLocators.BUTTON_CART), "Отсутствует кнопка добавления в корзину"
