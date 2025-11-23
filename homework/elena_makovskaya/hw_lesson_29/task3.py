# Напишите тест, который зайдет на страницу https://demoqa.com/dynamic-properties,
# нажмет на кнопку Color change только после того как она станет красной.

from playwright.sync_api import Page, expect, BrowserContext, Dialog

url = 'https://demoqa.com/dynamic-properties'


def test_click_btn_after_change_color(page: Page):
    page.goto(url)
    button = page.get_by_role('button', name='Color change')
    expect(button).to_have_class(['mt-4 text-danger btn btn-primary'])
    button.click()
