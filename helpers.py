from selenium import webdriver

class WebdriverFactory:

    @staticmethod
    def web_driver(browser_name):
        driver = None
        if browser_name == "firefox":
            driver = webdriver.Firefox()
        elif browser_name == "chrome":
            driver = webdriver.Chrome()
        return driver
