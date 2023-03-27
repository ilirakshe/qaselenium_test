import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def driver():
    options = Options()
    capabilities = DesiredCapabilities.CHROME
    capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
    # options.add_argument('--headless')  # we can use the headless flag for headless chrome
    # options.add_argument('--disable-gpu')  # turn off gpu if needed
    driver = webdriver.Chrome(options=options, desired_capabilities=capabilities)
    yield driver
    driver.quit()
