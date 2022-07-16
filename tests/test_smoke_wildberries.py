import pytest
from pages.wildberries import MainPage


def test_check_main_search(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser)

    page.search = 'iPhone 12'
    page.search_run_button.click()

    # Verify that user can see the list of products:
    assert page.products_titles.count() > 0


def test_check_wrong_input_in_search(web_browser):
    """ Make sure that wrong keyboard layout input works fine. """

    page = MainPage(web_browser)

    # Try to enter "футболка" with English keyboard:
    page.search = 'aen,jkrf'
    page.search_run_button.click()
    page.wait_page_loaded()

    # Verify that user can see the list of products:
    assert page.products_titles.count() == 105

    # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'футболка' in title.lower(), msg


def test_check_sort_by_price(web_browser):
    """ Make sure that sort by price works fine. """

    page = MainPage(web_browser)

    page.search = 'чайник'
    page.search_run_button.click()

    # Scroll to element before click on it to make sure
    # user will see this element in real browser
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()

    # Get prices of the products in Search results
    all_prices = page.products_prices.get_text()

    all_prices = [int(all_prices) for all_prices in all_prices if all_prices.isdigit()]
    print(all_prices)
    print(sorted(all_prices))

    # Make sure products are sorted by price correctly:
    assert all_prices == sorted(all_prices)


def test_all_goods_have_photo(web_browser):
    """ Make sure that all goods have a photo. """
    page = MainPage(web_browser)

    page.search = 'iphone 12'
    page.search_run_button.click()
    # Find the number of all photos of goods.
    count_img = page.product_image.count()

    count = 0
    # Check if the photo is loaded for goods
    for i in range(count_img):
        if page.product_image[i].get_attribute('src'):
            count += 1
    # Make sure that all goods have a photo
    assert count == count_img


@pytest.mark.xfail(reason="Not all goods have a rating")
def test_all_goods_have_name_rating(web_browser):
    """ Make sure that all goods have a rating.

     Note: this test case will fail because not all goods have a rating.
    """
    page = MainPage(web_browser)

    page.search = 'iPhone 12'
    page.search_run_button.click()
    # Get the number of goods per page
    count_name = page.product_name.count()
    # Get the number of goods, which have a rating
    count_rating = page.product_rating.count()
    # Make sure that all goods have a rating
    assert count_name == count_rating


def test_all_goods_have_delivery_period(web_browser):
    """ Make sure that all goods have a delivery period. """
    page = MainPage(web_browser)

    page.search = 'iPhone 12'
    page.search_run_button.click()
    # Get the number of goods per page
    count_name = page.product_name.count()
    # Get the number of goods, which have a delivery period
    count_delivery = page.product_delivery.count()
    # Make sure that all goods have a delivery period
    assert count_name == count_delivery


def test_adding_product_to_shoppinig_cart(web_browser):
    """ Make sure that element has been added to shopping cart"""
    page = MainPage(web_browser)
    # Search some good
    page.search = 'утюг'
    page.search_run_button.click()
    page.wait_page_loaded()
    # Select first item in search
    page.first_item_in_search_results.click()
    # Add item to shopping cart
    page.add_to_shopping_cart_btn.click()
    page.go_to_shopping_cart.click()
    # Make sure that good has been added to shopping cart
    assert page.header_one_basket.get_attribute("data-count") == '1'
