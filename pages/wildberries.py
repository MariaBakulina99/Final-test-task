#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "https://www.wildberries.ru/"

            super().__init__(web_driver, url)

    # Main search field
    search = WebElement(id='searchInput')

    # Search button
    search_run_button = WebElement(id='applySearchBtn')

    # Titles of the products in search results
    products_titles = ManyWebElements(class_name='goods-name')

    # Add to shopping cart button
    add_to_shopping_cart_btn = WebElement(css_selector='div > button:nth-child(2) > span.hide-mobile')

    # Button to sort products by price
    sort_products_by_price = WebElement(partial_link_text='Цене')

    # Prices of the products in search results
    products_prices = ManyWebElements(class_name='lower-price')

    # Images of the products in search results
    product_image = ManyWebElements(css_selector='div.product-card__img-wrap.img-plug.j-thumbnail-wrap > img')

    # Names of products in search results
    product_name = ManyWebElements(css_selector='div.product-card__brand-name > span')

    # Rating of products in search results
    product_rating = ManyWebElements(css_selector='a > span.product-card__rating.stars-line.star5')

    # Delivery period of products in search results
    product_delivery = ManyWebElements(css_selector='div > a > p')

    # Button of first banner in carousel
    btn_first_banner = WebElement(xpath='//li[@aria-label="Go to slide 1"]')

    # Button of second banner
    btn_second_banner = WebElement(xpath='//li[@aria-label="Go to slide 2"]')

    # Button of third banner
    btn_third_banner = WebElement(xpath='//li[@aria-label="Go to slide 3"]')

    # Button of fourth banner
    btn_fourth_banner = WebElement(xpath='//li[@aria-label="Go to slide 4"]')

    # Button of fifth banner
    btn_fifth_banner = WebElement(xpath='//li[@aria-label="Go to slide 5"]')

    # Button of sixth banner
    btn_sixth_banner = WebElement(xpath='//li[@aria-label="Go to slide 6"]')

    # Button of seventh banner
    btn_seventh_banner = WebElement(xpath='//li[@aria-label="Go to slide 7"]')

    # Button of eighth banner
    btn_eighth_banner = WebElement(xpath='//li[@aria-label="Go to slide 8"]')

    # Button of ninth banner
    btn_ninth_banner = WebElement(xpath='//li[@aria-label="Go to slide 9"]')

    # Button of tenth banner
    btn_tenth_banner = WebElement(xpath='//li[@aria-label="Go to slide 10"]')

    # Next slide button
    btn_next_slide = WebElement(xpath='//button[@aria-label="Next slide"]')

    # Previous slide button
    btn_previous_slide = WebElement(xpath='//button[@aria-label="Previous slide"]')

    # Element h1
    header_one = WebElement(css_selector='div.catalog-title-wrap > h1')

    # Element h1 at the page of basket
    header_one_basket = WebElement(xpath='//h1[@class="basket-section__header active"]')

    # Element h1 Barmariska page
    header_one_barmariska = WebElement(xpath='//h1[@class="brand-custom-header__name"]')

    # Banner oysho zara bershka
    oysho_zara_bershka = WebElement(xpath='//img[@alt="Zara, Bershka, OYSHO, Pull and Bear, Stradivarius, Massimo Dutti"]')

    # Banner vivienne sabo
    summer_with_garnier = WebElement(xpath='//img[@alt="сочное лето с GARNIER"]')

    # Banner Barmariska
    barmariska = WebElement(xpath='//img[@alt="Barmariska"]')

    # Banner DeFacto
    defacto = WebElement(xpath='//img[@alt="DeFacto"]')

    # Banner crocs
    crocs = WebElement(xpath='//img[@alt="CROCS"]')

    # Banner Vitek
    vitek = WebElement(xpath='//img[@alt="Скидки на технику VITEK"]')

    # Banner Belita
    belita = WebElement(xpath='//img[@alt="Белита-М"]')

    # Banner gulliver toys
    gulliver_toys = WebElement(xpath='//img[@alt="Гулливер игрушка"]')

    # Banner Mia Cara
    mia_cara = WebElement(xpath='//img[@alt="Mia Cara"]')

    # Banner crazy week electronics
    crazy_week_electronics = WebElement(xpath='//img[@alt="Сумасшедшая неделя: электроника"]')

    # Banner randez vous
    randez_vous = WebElement(xpath='//img[@alt="Tendance"]')

    # Banner ride with the wind
    ride_with_the_wind = WebElement(xpath='//img[@alt="Прокатись с ветерком  "]')

    # Banner fast delivery
    fast_delivery = WebElement(xpath='//img[@alt="Быстрая доставка: Краснодар"]')

    # Banner StarWind
    starwind = WebElement(xpath='//img[@alt="StarWind"]')

    # Banner frutonyanya
    frutonyaya = WebElement(xpath='//img[@alt="Фрутоняня"]')

    # Banner Adidas
    adidas = WebElement(xpath='//img[@alt="Adidas"]')

    # Banner Deco
    deco = WebElement(xpath='//img[@alt="Deco"]')

    # Banner L'oreal, Garnier
    loreal = WebElement(xpath='//img[@class="banner_57b3eb17-4d93-4349-9a79-437cedcf9db5"]')

    # Banner unilever
    unilever = WebElement(xpath='//img[@alt="Unilever"]')

    # Banner Himia
    himia = WebElement(xpath='//img[@alt="Himia"]')

    # Banner xiaomi
    xiaomi = WebElement(xpath='//img[@alt="Xiaomi, POCO"]')

    # Banner successful products
    successful_products = WebElement(xpath='//img[@alt="Удачные продукты"]')

    # Banner crazy week
    crazy_week = WebElement(xpath='//img[@alt="Сумасшедшая неделя"]')

    # Banner sale:clothes, shoes, accessories
    sale_clothes_shoes_accessories = WebElement(xpath='//img[@alt="РАСПРОДАЖА: Одежда, обувь, аксессуары"]')

    # Banner mango
    mango = WebElement(xpath='//img[@alt="Mango"]')

    # Banner fans
    fans = WebElement(xpath='//img[@alt="Вентиляторы"]')

    # Banner tasty sale
    tasty_sale = WebElement(xpath='//img[@alt="Вкусная распродажа"]')

    # Banner nanopyatki
    nanopyatki = WebElement(xpath='//img[@alt="Педикюр в домашних условиях"]')

    # Banner sokolov
    sokolov = WebElement(xpath='//img[@alt="Sokolov"]')

    # Banner scarlett
    scarlett = WebElement(xpath='//img[@alt="Scarlett"]')

    # Banner summer sale
    summer_sale = WebElement(xpath='//img[@alt="Unilever"]')

    # Banner unison
    unison = WebElement(xpath='//img[@alt="Унисон"]')

    # Banner Black Decker
    black_decker = WebElement(xpath='//img[@alt="Black+Decker садовая техника"]')

    # Banner Garnier
    garnier = WebElement(xpath='//img[@alt="Garnier"]')

    # Banner  HEAD & SHOULDERS
    head_and_shoulders = WebElement(xpath='//img[@alt=" HEAD & SHOULDERS"]')

    # Banner Yves Rocher
    yves_rocher = WebElement(xpath='//img[@alt="Скидки до 30% от Yves Rocher"]')

    # Banner Polaris
    polaris = WebElement(xpath='//img[@alt="Polaris"]')

    # Banner Demurya
    demurya = WebElement(xpath='//img[@alt="DEMURYA"]')

    # Banner lc_waikiki
    nestle = WebElement(xpath='//img[@alt="NESTLE"]')

    # Banner furniture on wb
    furniture_wb = WebElement(xpath='//img[@alt="Мебель"]')

    # Banner Geox
    geox = WebElement(xpath='//img[@alt="GEOX"]')

    # Button to change country
    change_country = WebElement(css_selector='li.simple-menu__item.j-b-header-country > span > span:nth-child(1)')

    # Radio bnt Armenia
    armenia = WebElement(css_selector='label:nth-child(3) > span.radio-with-text__decor')

    # Radio bnt Belarus
    belarus = WebElement(css_selector=' label:nth-child(4) > span.radio-with-text__decor')

    # Radio bnt Israel
    israel = WebElement(css_selector=' label:nth-child(5) > span.radio-with-text__decor')

    # Radio bnt Kazakhstan
    kazakhstan = WebElement(css_selector=' label:nth-child(6) > span.radio-with-text__decor')

    # Radio bnt Kyrgizystan
    kyrgizystan = WebElement(css_selector=' label:nth-child(7) > span.radio-with-text__decor')

    # Radio bnt uzbekistan
    uzbekistan = WebElement(css_selector=' label:nth-child(8) > span.radio-with-text__decor')

    # Delivery address (city)
    delivery_address = WebElement(xpath='//span[@data-wba-header-name="DLV_Adress"]')

    # Link to page about free_delivery
    free_delivery = WebElement(link_text='Бесплатная доставка')

    # Link to page about sell on wildberries
    sell_on_wildberries_btn = WebElement(link_text='Продавайте на Wildberries')

    # Link to page about work in wildberries
    work_in_wildberries_btn = WebElement(link_text='Работа в Wildberries')

    # Link to page about pickup points addresses
    adresess_btn = WebElement(link_text='Адреса')

    # Link to shopping cart page
    shopping_cart_btn = WebElement(xpath='//span[@class="navbar-pc__icon navbar-pc__icon--basket"]')
    # Link to page about how to make order
    how_to_make_order = WebElement(link_text='Как сделать заказ')

    # Link to page about payment methods
    payment_methods = WebElement(link_text='Способы оплаты')

    # Link to delivery page
    delivery = WebElement(link_text='Доставка')

    # Link to page about purchase returns
    purchase_returns = WebElement(link_text='Возврат товара')

    # Link to page about refunds
    refunds = WebElement(link_text='Возврат денежных средств')

    # Link to selling rules page
    selling_rules = WebElement(link_text='Правила продажи')

    # Link to page about rules trading platform
    rules_trading_platform = WebElement(link_text='Правила пользования торговой площадкой')

    # Link to questions and answers page
    questions_and_answers = WebElement(link_text='Вопросы и ответы')

    # Link to carriers page
    carriers = WebElement(link_text='Перевозчикам')

    # Link to page about opening pickup point
    open_pickup_point = WebElement(link_text='Откройте пункт выдачи')

    # Link to page about franchise
    franchise = WebElement(link_text='Франшизный пункт выдачи')

    # Link to wb guru page
    wb_guru = WebElement(link_text='WB Guru')

    # Link to employment page
    employment = WebElement(link_text='Трудоустройство')

    # Link to digital goods page
    digital_goods = WebElement(link_text='Цифровые товары')

    # Link to about us page
    about_us = WebElement(link_text='О нас')

    # Link to about us page
    requisites = WebElement(link_text='Реквизиты')

    # Link to press center page
    press_center = WebElement(link_text='Пресс-центр')

    # Link to contacts page
    contacts = WebElement(link_text='Контакты')

    # VK link
    vk_link = WebElement(link_text='Вконтакте')

    # Classmates link
    classmates_link = WebElement(link_text='Одноклассники')

    # Youtube link
    youtube_link = WebElement(link_text='YouTube')

    # Telegram link
    telegram_link = WebElement(link_text='Телеграм')

    # Google play link
    google_play_link = WebElement(class_name='google-play')

    # App store link
    app_store_link = WebElement(class_name='app-store')

    # App gallery link
    app_gallery_link = WebElement(class_name='app-gallery')

    # Link to bug bounty page
    bug_bounty = WebElement(link_text='Bug Bounty')

    # Link to compatibility check page
    compatibility_check = WebElement(link_text='Проверка совместимости')

    # Burger button
    burger = WebElement(xpath='//button[@data-wba-header-name="Catalog"]')

    # Menu element
    menu_burger = WebElement(xpath='//div[@class="menu-burger__main j-menu-burger-main j-menu-active"]')

    # Cross icon for menu burger
    cross_icon_menu_burger = WebElement(xpath='//button[@class="menu-burger__close j-close-menu-mobile"]')

    # Button that allows users to add goods to shopping card
    go_to_shopping_cart = WebElement(xpath='//a[@href="/lk/basket"]')

    # First item in search results
    first_item_in_search_results = WebElement(css_selector='div:nth-of-type(2) > img')
