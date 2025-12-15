import random

from playwright.sync_api import expect
from test_UI_emakovskaya_pw.pages.base_page import BasePage
from test_UI_emakovskaya_pw.pages.locators import multimedia_category_locators as loc


class OfficeDesigne(BasePage):
    page_url = '/shop/category/multimedia-9'

    def add_product_to_cart_and_verify(self):
        products = self.find(loc.result_products).element_handles()
        product_for_test = random.choice(products)
        product_for_test.click()

        product_title_on_page = self.find(loc.product_title_on_page_loc)
        add_to_cart_btn = self.find(loc.add_to_cart_button)
        add_to_cart_btn.click()
        expect(self.find(loc.product_counter)).to_have_text('1')
        self.find(loc.cart_button).click()
        product_title_on_cart = self.find(loc.product_title_on_cart_loc)
        name_from_cart_page = product_title_on_cart.text_content()
        expect(product_title_on_cart).to_have_text(name_from_cart_page)

    def change_currency_to_eur_and_verify(self):
        products = self.find(loc.result_products).element_handles()
        product_for_test = random.choice(products)
        product_for_test.click()

        self.find(loc.currency_dropdown).click()
        self.find(loc.currency_select_EUR).click()
        expect(self.find(loc.currency_price)).to_contain_text('€')

    def open_terms_and_conditions(self, text):
        products = self.find(loc.result_products).element_handles()
        product_for_test = random.choice(products)
        product_for_test.click()

        self.find(loc.terms_and_condition_link).click()
        tc_headline = self.find(loc.terms_headline)
        expect(tc_headline).to_have_text(text)
        # assert text in tc_headline

    def add_product_to_cart(self):
        products = self.find(loc.result_products).element_handles()
        product_for_test = random.choice(products)
        product_for_test.click()

        self.find(loc.add_to_cart_button).click()
        expect(self.find(loc.product_counter)).to_have_text('1')
