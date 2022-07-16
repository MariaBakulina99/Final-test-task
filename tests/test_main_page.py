from pages.wildberries import MainPage


def test_banner_oysho_zara_bershka(web_browser):
    """ Make sure that first banner in carousel redirects to the right page """
    page = MainPage(web_browser)
    page.btn_first_banner.click()
    page.oysho_zara_bershka.click()
    page.wait_page_loaded()

    assert page.header_one.get_text() == 'Zara, Bershka, OYSHO, Pull and Bear, Stradivarius, Massimo Dutti'


def test_banner_garnier(web_browser):
    """ Make sure that second banner in carousel redirects to the right page """
    page = MainPage(web_browser)
    page.btn_second_banner.click()
    page.garnier.click()
    page.wait_page_loaded()

    assert page.header_one.get_text() == 'Ambre Solaire от Garnier'


def test_banner_geox(web_browser):
    """ Make sure that third banner in carousel redirects to the right page """
    page = MainPage(web_browser)
    page.btn_third_banner.click()
    page.geox.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://www.wildberries.ru/brands/geox/all?sort=newly&cardsize=c516x688&page=1&fkind=2&bid=b0e63ca5-64c6-4d85-a1fe-df5e33c19e7d'


def test_banner_fast_delivery(web_browser):
    """ Make sure that fourth banner in carousel redirects to the right page """
    page = MainPage(web_browser)
    page.btn_fourth_banner.click()
    page.fast_delivery.click()
    page.wait_page_loaded()

    assert page.header_one.get_text() == 'Товары с быстрой доставкой: Краснодар'


def test_banner_crazy_week(web_browser):
    """ Make sure that fifth banner in carousel redirects to the right page """
    page = MainPage(web_browser)
    page.btn_next_slide.click()
    page.btn_next_slide.click()
    page.btn_fifth_banner.click()
    page.crazy_week.click()
    page.wait_page_loaded()

    assert page.header_one.get_text() == 'СУМАСШЕДШАЯ НЕДЕЛЯ'


def test_banner_crazy_week_electronics(web_browser):
    """ Make sure that sixth banner in carousel redirects to the right page """
    page = MainPage(web_browser)
    page.btn_next_slide.click()
    page.btn_next_slide.click()
    page.btn_next_slide.click()
    page.btn_sixth_banner.click()
    page.crazy_week_electronics.click()
    page.wait_page_loaded()

    assert page.header_one.get_text() == 'СУМАСШЕДШАЯ неделя: электроника и техника'


def test_banner_mango(web_browser):
    """ Make sure that seventh banner in carousel redirects to the right page """
    page = MainPage(web_browser)
    page.btn_next_slide.click()
    page.btn_next_slide.click()
    page.btn_next_slide.click()
    page.btn_next_slide.click()
    page.btn_seventh_banner.click()
    page.mango.click()
    page.wait_page_loaded()

    assert page.header_one.get_text() == 'MANGO: скидки до -50%'


def test_banner_crazy_week_Electronic(web_browser):
    """ Make sure that eighth banner in carousel redirects to the right page """
    page = MainPage(web_browser)
    page.btn_next_slide.click()
    page.btn_next_slide.click()
    page.btn_next_slide.click()
    page.btn_next_slide.click()
    page.btn_next_slide.click()
    page.btn_eighth_banner.click()
    page.crazy_week_electronics.click()
    page.wait_page_loaded()

    assert page.header_one.get_text() == 'уДачные продукты'


def test_banner_xiaomi(web_browser):
    """ Make sure that xiaomi banner redirects to the right page """
    page = MainPage(web_browser)
    page.xiaomi.click()
    page.wait_page_loaded()

    assert page.header_one.get_text() == 'Смартфоны Xiaomi и POCO'


def test_banner_starwind(web_browser):
    """ Make sure that starwind banner redirects to the right page """
    page = MainPage(web_browser)
    page.starwind.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://www.wildberries.ru/brands/starwind/all?bid=b1d534a7-610d-4504-a076-75c3e9ab39e6'


def test_banner_frutonyaya(web_browser):
    """ Make sure that frutonyaya banner redirects to the right page """
    page = MainPage(web_browser)
    page.frutonyaya.click()
    page.wait_page_loaded()

    assert page.header_one.get_text() == 'ФрутоНяня детское питание'


def test_banner_adidas(web_browser):
    """ Make sure that adidas banner redirects to the right page """
    page = MainPage(web_browser)
    page.adidas.click()
    page.wait_page_loaded()

    assert page.header_one.get_text() == 'Adidas'


def test_banner_deco(web_browser):
    """ Make sure that deco banner redirects to the right page """
    page = MainPage(web_browser)
    page.scroll_down(900)
    page.deco.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://www.wildberries.ru/brands/deko?bid=70555af5-259c-4b01-b0c2-f59d904c03f0'


def test_banner_unilever(web_browser):
    """ Make sure that unilever banner redirects to the right page """
    page = MainPage(web_browser)
    page.scroll_down(900)
    page.unilever.click()
    page.wait_page_loaded()

    assert page.header_one.get_text() == 'Unilever'


def test_banner_himia(web_browser):
    """ Make sure that himia banner redirects to the right page """
    page = MainPage(web_browser)
    page.scroll_down(900)
    page.himia.click()
    page.wait_page_loaded()

    assert page.header_one.get_text() == 'P&G'


def test_banner_crocs(web_browser):
    """ Make sure that Crocs banner redirects to the right page """
    page = MainPage(web_browser)
    page.scroll_down(1200)
    page.wait_page_loaded()
    page.crocs.click()
    page.wait_page_loaded()

    assert page.header_one.get_text() == 'CROCS горячая распродажа скидки до 60%'


def test_banner_polaris(web_browser):
    """ Make sure that Polaris banner redirects to the right page """
    page = MainPage(web_browser)
    page.scroll_down(1200)
    page.wait_page_loaded()
    page.polaris.click()
    page.wait_page_loaded()

    assert page.header_one.get_text() == 'Polaris для дома'


def test_banner_demurya(web_browser):
    """ Make sure that Demurya banner redirects to the right page """
    page = MainPage(web_browser)
    page.scroll_down(1500)
    page.wait_page_loaded()
    page.demurya.click()
    page.wait_page_loaded()

    assert page.header_one.get_text() == 'Летний SALE от DEMURYA'


def test_banner_furniture_wb(web_browser):
    """ Make sure that furniture banner redirects to the right page """
    page = MainPage(web_browser)
    page.scroll_down(1500)
    page.wait_page_loaded()
    page.furniture_wb.click()
    page.wait_page_loaded()

    assert page.header_one.get_text() == 'Мебель'
