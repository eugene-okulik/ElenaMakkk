from playwright.sync_api import expect
from test_UI_emakovskaya_pw.pages.base_page import BasePage
from test_UI_emakovskaya_pw.pages.locators import section_desc_locators as loc


class Section_Desc_Page(BasePage):
    page_url = '/shop/category/desks-1'

    def search_items_and_verify(self, text):
        search_field = self.find(loc.search_field)
        search_field.fill(text)
        search_field.press('Enter')
        expect(self.find(loc.result_count)).to_contain_text('found')

        products_locator = self.find(loc.result_products)

        for element in products_locator.element_handles():
            content = element.text_content()
            assert text in content, f'Продукт "{content}" не содержит в названии текста "{text}"'


    def sort_items_by_name_and_verify(self):
        dropdown = self.find(loc.sort_dropdown)
        dropdown.click()
        sorting_by_name = self.find(loc.sort_by_name)
        sorting_by_name.click()
        results = self.find(loc.result_products).element_handles()
        product_names = []
        for product in results:
            name = product.text_content()
            if name:
                product_names.append(name.strip())
        sorted_names = sorted(product_names)
        assert product_names == sorted_names

    def filter_by_price_and_verify(self, min_price, max_price):
        self.find(loc.field_min).first.click()
        min_price_set = self.find(loc.input_min).first
        min_price_set.click()
        min_price_set.fill(min_price)
        min_price_set.press('Enter')

        self.find(loc.field_max).first.click()
        max_price_set = self.find(loc.input_max).first
        max_price_set.click()
        max_price_set.fill(max_price)
        max_price_set.press('Enter')

        results = self.find(loc.product_price).element_handles()
        for item in results:
            price_attr = item.text_content()
            price_result = float(price_attr.replace(',', ''))
            assert float(max_price) >= price_result >= float(min_price)
