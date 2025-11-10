# Напишите программу, которая зайдет на страницу https://demoqa.com/automation-practice-form и
# полностью заполнит форму (кроме загрузки файла) и нажмет Submit.
#
# Небольшая особенность
# Страничка эта немного кривая, иногда реклама перекрывает элементы и по ним невозможно кликнуть
# (но сейчас, смотрю, вообще реклама пропала). Если бы это было приложение, которое мы тестируем, это был бы баг.
# Но работаем с тем, что есть. И для нас это даже плюс, нужно найти как выкрутиться.
# Обойти это можно уменьшив размер экрана браузера - тогда элементы перераспределяются и становятся доступны.
# Но если реклама так и не появится, то ничего на странице не мешает.
#
# После отправки вам будет отображено окошко с тем что вы ввели. Получите со страницы содержимое этого окошка и
# распечатайте (выведите на экран).

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

base_url = 'https://demoqa.com/automation-practice-form'
first_name = 'Elena'
last_name = 'Makovskaya'
email = 'test@gmail.com'
mobile = '2911122333'
subjects = 'Maths'
current_address = 'Minsk'
dob_year = '1991'
dob_month = 'August'
state = 'NCR'
city = 'Delhi'


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.set_window_size(1200, 1000)
    driver.implicitly_wait(5)
    return driver


def test_practice_form(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(base_url)
    driver.execute_script("window.scrollTo(0, 200);")

    first_name_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#firstName')))
    first_name_field.send_keys(first_name)
    last_name_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#lastName')))
    last_name_field.send_keys(last_name)
    email_field = wait.until(EC.element_to_be_clickable((By.ID, 'userEmail')))
    email_field.send_keys(email)

    gender_label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[for = "gender-radio-2"]')))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", gender_label)
    gender_label.click()

    mobile_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#userNumber')))
    mobile_field.send_keys(mobile)

    calendar = wait.until(EC.element_to_be_clickable((By.ID, 'dateOfBirthInput')))
    calendar.click()
    year = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__year-select')
    select_year = Select(year)
    select_year.select_by_value(dob_year)
    month = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__month-select')
    select_month = Select(month)
    select_month.select_by_index(7)
    date = driver.find_element(
        By.CSS_SELECTOR, '[aria-label="Choose Monday, August 5th, 1991"]'
    )
    date.click()

    subjects_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#subjectsInput')))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", subjects_field)
    subjects_field.send_keys(subjects)
    subjects_field.send_keys(Keys.ENTER)

    reading_checkbox_label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[for = "hobbies-checkbox-1"]')))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", reading_checkbox_label)
    reading_checkbox_label.click()

    current_address_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#currentAddress')))
    current_address_field.send_keys(current_address)

    select_state_input = wait.until(EC.element_to_be_clickable((By.ID, 'react-select-3-input')))
    select_state_input.send_keys(state)
    select_state_input.send_keys(Keys.ENTER)

    wait.until_not(EC.presence_of_element_located((By.CSS_SELECTOR, '#state > div.css-26l3qy-menu')))
    select_city_input = wait.until(EC.element_to_be_clickable((By.ID, 'react-select-4-input')))
    select_city_input.send_keys(city)
    select_city_input.send_keys(Keys.ENTER)

    submit_btn = wait.until(EC.element_to_be_clickable((By.ID, 'submit')))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
    submit_btn.click()

    result_modal = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-dialog')))
    result = result_modal.text
    print(result)
