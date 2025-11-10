# Первый тест
# http://testshop.qa-practice.com/
#
# откройте первый (Customizable Desk) товар в новой вкладке
# Перейдите на вкладку с товаром
# Добавьте товар в корзину
# Нажмите на кнопку Add to Cart
# В открывшемся попапе нажмите Continue shopping
# Закройте вкладку с товаром
# На начальной вкладке откройте корзину
# Убедитесь, что в корзине тот товар, который вы добавляли
# Второй тест
# На том же сайте
#
# зайти на сайт http://testshop.qa-practice.com/
# навести мышку на первый товар (на картинку товара)
# нажать появившуюся кнопку корзины
# в появившемся попапе проверить, что товар, на котором нажимали кнопку корзины, появился в этом попапе

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

base_url = 'http://testshop.qa-practice.com/'


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(6)
    return chrome_driver


def test_first(driver):
    wait = WebDriverWait(driver, 5)
    driver.get(base_url)
    link = driver.find_element(By.LINK_TEXT, 'Customizable Desk')
    ActionChains(driver).key_down(Keys.COMMAND).click(link).key_up(Keys.COMMAND).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    add_to_cart_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#add_to_cart')))
    add_to_cart_btn.click()
    wait.until(EC.visibility_of_element_located((By.ID, 'add_to_cart')))
    continue_shopping = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-secondary')))
    continue_shopping.click()
    driver.switch_to.window(tabs[0])
    driver.refresh()
    cart = driver.find_element(By.CSS_SELECTOR, '.fa-shopping-cart')
    cart.click()
    product = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Customizable Desk')))
    assert 'Customizable Desk' in product.text


def test_second(driver):
    wait = WebDriverWait(driver, 5)
    driver.get(base_url)
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[alt="Customizable Desk"]')))
    ActionChains(driver).move_to_element(element).perform()
    cart = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="12"]/following::a[1]')))
    cart.click()
    product_in_cart = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//td[@class="td-product_name"]/child :: strong')
        )
    )
    assert 'Customizable Desk' in product_in_cart.text
