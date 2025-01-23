
import pytest

from selenium import webdriver

class WebdriverFactory:

    @staticmethod
    @pytest.mark.parametrize('browser_name', ['chrome', 'firefox'])
    def web_driver(browser_name):
        if browser_name == "firefox":
            return webdriver.Firefox()
        elif browser_name == "chrome":
            return webdriver.Chrome()