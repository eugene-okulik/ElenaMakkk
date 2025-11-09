# Часть 1
# Напишите тест, который заходит на страницу https://www.qa-practice.com/elements/select/single_select,
# выбирает какой-нибудь вариант из Choose language, кликает Submit и проверяет,
# что в окошке с результатом отображается тот вариант, который был выбран.
#
# Часть 2
# Напишите тест, который зайдет на страницу https://the-internet.herokuapp.com/dynamic_loading/2, нажмет Start,
# и проверит, что на странице появляется текст "Hello World!"


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

url1 = 'https://www.qa-practice.com/elements/select/single_select'
url2 = 'https://the-internet.herokuapp.com/dynamic_loading/2'


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def test_select_lng(driver):
    my_lng = 'Python'
    wait = WebDriverWait(driver, 10)
    driver.get(url1)
    select = wait.until(EC.presence_of_element_located((By.ID, 'id_choose_language')))
    select_lng = Select(select)
    select_lng.select_by_visible_text(my_lng)
    submit_btn = wait.until(EC.element_to_be_clickable((By.ID, 'submit-id-submit')))
    submit_btn.click()
    result = wait.until(EC.presence_of_element_located((By.ID, 'result-text')))
    assert my_lng == result.text


def test_button_start(driver):
    text_finish = 'Hello World!'
    wait = WebDriverWait(driver, 10)
    driver.get(url2)
    start_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#start > button')))
    start_btn.click()

    finish_txt = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#finish > h4')))
    assert text_finish == finish_txt.text
