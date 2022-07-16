from pages.wildberries import MainPage


def test_check_how_to_make_order(web_browser):
    """Make sure that link redirects to page about how to make order"""
    page = MainPage(web_browser)
    page.scroll_down()
    page.how_to_make_order.click()

    assert page.get_current_url() == 'https://www.wildberries.ru/services/kak-sdelat-zakaz'


def test_payment_methods(web_browser):
    """Make sure that link redirects to page about payment methods"""
    page = MainPage(web_browser)
    page.scroll_down()
    page.payment_methods.click()

    assert page.get_current_url() == 'https://www.wildberries.ru/services/sposoby-oplaty'


def test_delivery(web_browser):
    """Make sure that link redirects to page about delivery"""
    page = MainPage(web_browser)
    page.scroll_down()
    page.delivery.click()

    assert page.get_current_url() == 'https://www.wildberries.ru/services/besplatnaya-dostavka'


def test_purchase_returns(web_browser):
    """Make sure that link redirects to page about purchase returns"""
    page = MainPage(web_browser)
    page.scroll_down()
    page.purchase_returns.click()

    assert page.get_current_url() == 'https://www.wildberries.ru/services/vozvrat-tovara'


def test_refunds(web_browser):
    """Make sure that link redirects to page about refunds"""
    page = MainPage(web_browser)
    page.scroll_down()
    page.refunds.click()

    assert page.get_current_url() == 'https://www.wildberries.ru/services/vozvrat-denezhnyh-sredstv'


def test_selling_rules(web_browser):
    """Make sure that link redirects to page about selling rules"""
    page = MainPage(web_browser)
    page.scroll_down()
    page.selling_rules.click()

    assert page.get_current_url() == 'https://www.wildberries.ru/services/pravila-prodazhi'


def test_rules_of_trading_platform(web_browser):
    """Make sure that link redirects to page about rules of trading platform"""
    page = MainPage(web_browser)
    page.scroll_down()
    page.rules_trading_platform.click()

    assert page.get_current_url() == 'https://www.wildberries.ru/services/pravila-polzovaniya-torgovoy-ploshchadkoy'


def test_questions_and_answers(web_browser):
    """Make sure that link redirects to questions and answers page"""
    page = MainPage(web_browser)
    page.scroll_down()
    page.questions_and_answers.click()

    assert page.get_current_url() == 'https://www.wildberries.ru/services/voprosy-i-otvety'


def test_compatibility_check(web_browser):
    """Make sure that link redirects to compatibility check page"""
    page = MainPage(web_browser)
    page.compatibility_check.click()
    page.scroll_down()

    assert page.get_current_url() == 'https://www.wildberries.ru/services/proverka-sovmestimosti'


def test_carries(web_browser):
    """Make sure that link redirects to carries page"""
    page = MainPage(web_browser)
    page.scroll_down()
    page.carriers.click()
    page.switch_to_window(window_number=1)

    assert page.get_current_url() == 'https://www.wildberries.ru/promo/priglashaem-k-sotrudnichestvu'


def test_open_pickup_point(web_browser):
    """Make sure that link redirects to page about opening pickup point"""
    page = MainPage(web_browser)
    page.scroll_down()
    page.open_pickup_point.click()
    page.switch_to_window(window_number=1)

    assert page.get_current_url() == 'https://point-promo.wb.ru/'


def test_franchise(web_browser):
    """Make sure that link redirects to franchise page"""
    page = MainPage(web_browser)
    page.scroll_down()
    page.franchise.click()
    page.switch_to_window(window_number=1)

    assert page.get_current_url() == 'https://www.wildberries.ru/services/franshizniy-punkt-vydachi'


def test_wb_guru(web_browser):
    """Make sure that link redirects to wb guru page"""
    page = MainPage(web_browser)
    page.scroll_down()
    page.wb_guru.click()
    page.switch_to_window(window_number=1)

    assert page.get_current_url() == 'https://guru.wildberries.ru/?utm_source=main_footer'


def test_employment(web_browser):
    """Make sure that link redirects to page about employment"""
    page = MainPage(web_browser)
    page.scroll_down()
    page.employment.click()
    page.switch_to_window(window_number=1)

    assert page.get_current_url() == 'https://vsemrabota.ru/appwb'


def test_digital_goods(web_browser):
    """Make sure that link redirects to page about digital goods"""
    page = MainPage(web_browser)
    page.scroll_down()
    page.digital_goods.click()
    page.switch_to_window(window_number=1)

    assert page.get_current_url() == 'https://digital.wildberries.ru/'


def test_about_us(web_browser):
    """Make sure that link redirects to about us page"""
    page = MainPage(web_browser)
    page.scroll_down()
    page.about_us.click()

    assert page.get_current_url() == 'https://www.wildberries.ru/services/o-nas'


def test_requisites(web_browser):
    """Make sure that link redirects to requisites page"""
    page = MainPage(web_browser)
    page.scroll_down()
    page.requisites.click()

    assert page.get_current_url() == 'https://www.wildberries.ru/services/rekvizity'


def test_press_center(web_browser):
    """Make sure that link redirects to press center page"""
    page = MainPage(web_browser)
    page.scroll_down()
    page.press_center.click()

    assert page.get_current_url() == 'https://www.wildberries.ru/presscenter'


def test_contacts(web_browser):
    """Make sure that link redirects to contacts page"""
    page = MainPage(web_browser)
    page.scroll_down()
    page.contacts.click()

    assert page.get_current_url() == 'https://www.wildberries.ru/services/kontakty'


def test_bug_bounty(web_browser):
    """Make sure that link redirects to bug bounty page"""
    page = MainPage(web_browser)
    page.scroll_down()
    page.bug_bounty.click()

    assert page.get_current_url() == 'https://www.wildberries.ru/services/bug-bounty'


def test_vk_link(web_browser):
    """Make sure that link redirects to vk """
    page = MainPage(web_browser)
    page.scroll_down()
    page.vk_link.click()
    page.switch_to_window(window_number=1)

    assert page.get_current_url() == 'https://vk.com/public9695053'


def test_classmates_link(web_browser):
    """Make sure that link redirects to classmates """
    page = MainPage(web_browser)
    page.scroll_down()
    page.classmates_link.click()
    page.switch_to_window(window_number=1)

    assert page.get_current_url() == 'https://ok.ru/wildberries'


def test_youtube_link(web_browser):
    """Make sure that link redirects to youtube """
    page = MainPage(web_browser)
    page.scroll_down()
    page.youtube_link.click()
    page.switch_to_window(window_number=1)

    assert page.get_current_url() == 'https://www.youtube.com/c/wildberries'


def test_telegram_link(web_browser):
    """Make sure that link redirects to telegram """
    page = MainPage(web_browser)
    page.scroll_down()
    page.telegram_link.click()
    page.switch_to_window(window_number=1)

    assert page.get_current_url() == 'https://t.me/wildberriesru_official'


def test_google_play_link(web_browser):
    """Make sure that link redirects to google play"""
    page = MainPage(web_browser)
    page.scroll_down()
    page.google_play_link.click()
    page.switch_to_window(window_number=1)

    assert page.get_current_url() == 'https://play.google.com/store/apps/details?id=com.wildberries.ru'


def test_app_store_link(web_browser):
    """Make sure that link redirects to app store """
    page = MainPage(web_browser)
    page.scroll_down()
    page.app_store_link.click()
    page.switch_to_window(window_number=1)

    assert page.get_current_url() == 'https://apps.apple.com/ru/app/wildberries/id597880187'


def test_app_gallery_link(web_browser):
    """Make sure that link redirects to app gallery"""
    page = MainPage(web_browser)
    page.scroll_down()
    page.app_gallery_link.click()
    page.switch_to_window(window_number=1)

    assert page.get_current_url() == 'https://appgallery.huawei.com/#/app/C101183325'


def test_compatibility_check(web_browser):
    """Make sure that link redirects to compatibility check page """
    page = MainPage(web_browser)
    page.scroll_down()
    page.compatibility_check.click()

    assert page.get_current_url() == 'https://www.wildberries.ru/services/proverka-sovmestimosti'
