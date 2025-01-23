import pytest

from helpers import WebdriverFactory

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    driver = WebdriverFactory().web_driver(request.param)
    yield driver
    driver.quit()
