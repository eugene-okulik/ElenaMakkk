# Напишите тест, который зайдет на страницу https://www.qa-practice.com/elements/new_tab/button,
# нажмет на кнопку Click, в открывшемся табе проверит,
# что в результате написано "I am a new page in a new tab" и проверит,
# что на изначальной вкладке кнопка Click - активна (enabled)


from playwright.sync_api import Page, expect, BrowserContext, Dialog

url = 'https://www.qa-practice.com/elements/new_tab/button'


def test_new_tab_check_msq_and_return_back_check_btn(page: Page, context: BrowserContext):
    page.goto(url)
    link = page.locator('#new-page-button')
    with context.expect_page() as new_page_event:
        link.click()
    new_page = new_page_event.value
    result = new_page.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    new_page.close()
    button_on_previous_page = page.get_by_role('link', name='Click')
    expect(button_on_previous_page).to_be_enabled()
