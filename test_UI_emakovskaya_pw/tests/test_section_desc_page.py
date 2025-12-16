def test_search_items(section_desc):
    section_desc.open_page()
    section_desc.search_items_and_verify('Corner')


def test_sort_items_by_name(section_desc):
    section_desc.open_page()
    section_desc.sort_items_by_name_and_verify()


def test_filter_products_by_price(section_desc):
    section_desc.open_page()
    section_desc.filter_by_price_and_verify(min_price='100', max_price='3000')
