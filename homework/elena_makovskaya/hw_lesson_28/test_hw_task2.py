from playwright.sync_api import Page, expect

url = 'https://demoqa.com/automation-practice-form'

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


def test_practice_form(page: Page):
    page.goto(url)
    page.get_by_placeholder('First Name').fill(first_name)
    page.get_by_placeholder('Last Name').fill(last_name)
    page.get_by_placeholder('name@example.com').fill(email)
    page.get_by_text('Female').click()
    page.get_by_placeholder('Mobile Number').fill(mobile)
    page.locator('#dateOfBirthInput').click()
    page.locator('.react-datepicker__year-select').select_option(dob_year)
    page.locator('.react-datepicker__month-select').select_option(dob_month)
    page.locator('[aria-label="Choose Monday, August 5th, 1991"]').click()
    subject_field = page.locator('#subjectsInput')
    subject_field.fill(subjects)
    subject_field.press('Enter')
    page.get_by_text('Reading').click()
    page.get_by_placeholder('Current Address').fill(current_address)
    state_dropdown = page.locator('#react-select-3-input')
    state_dropdown.fill(state)
    state_dropdown.press('Enter')
    city_dropdown = page.locator('#react-select-4-input')
    city_dropdown.fill(city)
    city_dropdown.press('Enter')
    page.get_by_role('button', name="Submit").click()
