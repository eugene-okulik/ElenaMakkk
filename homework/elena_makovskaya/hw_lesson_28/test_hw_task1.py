from playwright.sync_api import Page, expect

url = 'https://the-internet.herokuapp.com/'
login = 'testLogin'
password = 'test_password'


def test_get_by_role(page: Page):
    page.goto(url)
    page.get_by_role('link', name='Form Authentication').click()

    login_input = page.get_by_role('textbox', name='username')
    login_input.fill(login)

    password_input = page.get_by_role('textbox', name='password')
    password_input.fill(password)

    page.get_by_role('button').click()
