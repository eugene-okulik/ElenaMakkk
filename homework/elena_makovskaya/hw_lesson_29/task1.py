# Напишите тест, который заходит на страницу https://www.qa-practice.com/elements/alert/confirm,
# кликает на кнопку, чтобы появился алерт, жмет Ok и проверяет, что на страние в секции "You selected" написано "Ok"


from playwright.sync_api import Page, expect, BrowserContext, Dialog
from time import sleep

url = 'https://www.qa-practice.com/elements/alert/confirm'


def test_click_alert_and_verify_message(page: Page):
    page.on('dialog', lambda alert: alert.accept())
    page.goto(url)
    page.get_by_role('link', name='Click').click()
    result_text = page.locator('#result-text')
    expect(result_text).to_have_text('Ok')
    sleep(3)
