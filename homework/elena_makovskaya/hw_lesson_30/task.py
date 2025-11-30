# Напишите тест, который заходит на страницу https://www.apple.com/shop/buy-iphone,
# кликает по iPhone 17 Pro & iPhone 17 Pro Max, в открывшемся попапе проверяет заголовок.
#
# Но не всё так просто. )))
# Перед открытием страницы включите отлавливание запроса в котором приходит информация о товарах и
# измените ответ так так, чтобы iPhone 17 Pro в попапе назывался "яблокофон 17 про"
#
# Попробуйте самостоятельно поискать сам запрос и где что нужно подменить в ответе на этот запрос.
# Вам в помощь всякие онлайн отображатели json, чтобы было проще разобраться в структуре ответа.
# Я обычно пользуюсь https://jsoneditoronline.org/
#
# Если совсем не получится разобраться, пишите мне в личку, подскажу.
#
# Ну и при проверке заголовка в попапе проверяйте, что заголовок = тому, на что вы заменили название телефона.


import json

from playwright.sync_api import Page, expect, Route

url = 'https://www.apple.com/shop/buy-iphone'
following_url = '**/digital-mat**'
new_title = 'яблокофон 17 про'


def test_verify_iphone_title(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = new_title
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )

    page.route(following_url, handle_route)
    page.goto(url)
    page.locator('[data-relatedlink=":ra:_secondarybutton"]').click()
    title = page.locator('[data-autom="DigitalMat-overlay-header-0-0"]')
    expect(title).to_have_text(new_title)
