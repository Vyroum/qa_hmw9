import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="session", autouse=True)
def browser_set():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = "eager"
    browser.config.base_url = "https://demoqa.com"
    browser.driver.maximize_window()

    yield
    browser.quit()
