Introduction

This repository contains automated tests for the wildberries online store.

Files

conftest.py contains all the required code to catch failed test cases and make screenshot of the page in case any test case will fail.

pages/base.py contains PageObject pattern implementation for Python.

pages/elements.py contains helper class to define web elements on web pages.

tests/test_smoke_wildberries.py contains several smoke Web UI tests for YandexMarket (https://www.wildberries.ru/)

tests/test_footer.py contains main page several footer tests (https://www.wildberries.ru/)

tests/test_header.py contains main page several header tests (https://www.wildberries.ru/)

tests/test_main_page.py contains main page several main page tests (https://www.wildberries.ru/)

How To Run Tests

Install all requirements:

pip3 install -r requirements
Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

Run tests:

python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/

Note: ~/chrome in this example is the file of Selenium WebDriver downloaded and unarchived on step #2.
