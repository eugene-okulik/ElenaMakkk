import random
import re

from playwright.sync_api import expect
from test_UI_emakovskaya_pw.pages.base_page import BasePage
from test_UI_emakovskaya_pw.pages.locators import cart_page_locators as loc


class CartPage(BasePage):
    page_url = '/shop/cart'
    text = 'Your cart is empty!'

    def empty_cart_message(self, text=None):
        text = text if text else self.text
        empty_msg_text = self.find(loc.empty_message)
        expect(empty_msg_text).to_have_text(text)

    def change_product_quantity_and_verify_total_price(self):
        one_product_price_text = self.find(loc.product_price).text_content()
        match = re.search(r"([\d,\.]+)", one_product_price_text.replace(',', '.'))
        if not match:
            raise ValueError("Не удалось найти цену за продукт")
        one_product_price_str = match.group(1)
        one_product_price = float(one_product_price_str)

        quantity = random.randint(1, 3)
        quantity_field = self.find(loc.quantity_input)
        quantity_field.click()
        quantity_field.fill('')
        quantity_field.fill(str(quantity))
        quantity_field.press('Enter')

        final_price_text = self.find(loc.product_price).text_content()
        match = re.search(r"([\d,\.]+)", final_price_text.replace(',', '.'))
        if not match:
            raise ValueError("Не удалось найти итоговую цену")
        expected_price = round(one_product_price * quantity, 2)
        expect(self.find(loc.product_price)).to_have_text(f"{expected_price:.2f}")

    def check_invalid_promo(self):
        promo = 'test'
        input_promo = self.find(loc.discount_code)
        input_promo.click()
        input_promo.fill(promo)
        input_promo.press('Enter')
        expect(self.find(loc.error_message)).to_have_text('This promo code is not available.')
