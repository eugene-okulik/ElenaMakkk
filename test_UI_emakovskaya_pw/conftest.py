import pytest

from test_UI_emakovskaya_pw.pages.cart_page import CartPage
from test_UI_emakovskaya_pw.pages.multimedia_category_products_page import OfficeDesigne
from test_UI_emakovskaya_pw.pages.section_desc_page import Section_Desc_Page


@pytest.fixture()
def section_desc(page):
    return Section_Desc_Page(page)


@pytest.fixture()
def cart_page(page):
    return CartPage(page)


@pytest.fixture()
def office_designe(page):
    return OfficeDesigne(page)
