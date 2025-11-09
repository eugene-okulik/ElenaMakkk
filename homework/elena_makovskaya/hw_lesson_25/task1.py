# Напишите программку, которая заходит на вот эту страницу: https://www.qa-practice.com/elements/input/simple,
# вводит какой-то текст в поле, делает submit , а после этого находит элемент, в котором отображается тот текст,
# который был введен и рапечатывает этот текст.
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = 'https://www.qa-practice.com/elements/input/simple'


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def test_submit_text(driver):
    input_data = 'Hello'
    driver.get(base_url)
    input_field = driver.find_element(By.CSS_SELECTOR, '#id_text_string')
    input_field.send_keys(input_data)
    input_field.send_keys(Keys.ENTER)
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'result-text')))
    result_field = driver.find_element(By.CLASS_NAME, 'result-text')
    print(result_field.text)
