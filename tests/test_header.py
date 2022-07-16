from pages.wildberries import MainPage


def test_change_counry_to_armenia(web_browser):
    """ Make sure it is possible to change the country to Armenia"""
    page = MainPage(web_browser)
    page.change_country.click()
    page.armenia.click()

    assert page.get_current_url() == 'https://am.wildberries.ru/'


def test_change_counry_to_belarus(web_browser):
    """ Make sure it is possible to change the country to Belarus"""
    page = MainPage(web_browser)
    page.change_country.click()
    page.belarus.click()

    assert page.get_current_url() == 'https://by.wildberries.ru/'


def test_change_counry_to_israel(web_browser):
    """ Make sure it is possible to change the country to Israel"""
    page = MainPage(web_browser)
    page.change_country.click()
    page.israel.click()

    assert page.get_current_url() == 'https://wildberries.co.il/'


def test_change_counry_to_kazakhstan(web_browser):
    """ Make sure it is possible to change the country to Kazakhstan"""
    page = MainPage(web_browser)
    page.change_country.click()
    page.kazakhstan.click()

    assert page.get_current_url() == 'https://kz.wildberries.ru/'


def test_change_counry_to_kyrgizystan(web_browser):
    """ Make sure it is possible to change the country to Kyrgizystan"""
    page = MainPage(web_browser)
    page.change_country.click()
    page.kyrgizystan.click()

    assert page.get_current_url() == 'https://kg.wildberries.ru/'


def test_change_country_to_uzbekistan(web_browser):
    """ Make sure it is possible to change the country to Uzbekistan"""
    page = MainPage(web_browser)
    page.change_country.click()
    page.uzbekistan.click()

    assert page.get_current_url() == 'https://uz.wildberries.ru/'


def test_free_delivery(web_browser):
    """ Make sure that link redirects to free delivery page """
    page = MainPage(web_browser)
    page.free_delivery.click()

    assert page.get_current_url() == 'https://www.wildberries.ru/services/besplatnaya-dostavka?desktop=1'


def test_check_employment_btn(web_browser):
    """ Make sure that link redirects to employment page """
    page = MainPage(web_browser)
    page.work_in_wildberries_btn.click()

    assert page.get_current_url() == 'https://www.wildberries.ru/services/trudoustroystvo'


def test_menu_burger_btn(web_browser):
    """ Make sure menu burger btn allows user to open menu """
    page = MainPage(web_browser)
    page.burger.click()
    page.wait_page_loaded()

    assert page.menu_burger.is_visible()


def test_close_menu_burger(web_browser):
    """ Make sure it is possible to close menu burger """
    page = MainPage(web_browser)
    page.burger.click()
    page.wait_page_loaded()
    page.cross_icon_menu_burger.click()

    assert page.menu_burger.is_visible() is False


def test_check_address_btn(web_browser):
    """ Make sure it is possible to open page about addresses of  pick points"""
    page = MainPage(web_browser)
    page.adresess_btn.click()
    assert page.get_current_url() == 'https://www.wildberries.ru/services/besplatnaya-dostavka?desktop=1#terms-delivery'


def test_check_shopping_cart_btn(web_browser):
    """ Make sure it is possible to open shopping cart page"""
    page = MainPage(web_browser)
    page.shopping_cart_btn.click()
    assert page.get_current_url() == 'https://www.wildberries.ru/lk/basket'
