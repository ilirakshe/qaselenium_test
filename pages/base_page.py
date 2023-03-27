import json

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.baaqmd.gov"

    def get(self, endpoint=None):
        if endpoint:
            return self.driver.get(f"{self.base_url}{endpoint}")
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def get_current_url(self):
        return self.driver.current_url

    # VERY BAD AND UGLY THING. We can move out this checks and use list of elements for selection. Don't do this
    # like me. Never.
    def get_logo(self):
        try:
            assert self.driver.find_element(By.CSS_SELECTOR, ".top-logo")
        except NoSuchElementException:
            try:
                assert self.driver.find_element(By.CSS_SELECTOR, ".login-logo")
            except NoSuchElementException:
                assert self.driver.find_element(By.CSS_SELECTOR, ".logo-one")

        return True

    # here we can use requests library for sending request to url and retriving status code but we love complex ways.
    def get_status_code(self, url):
        for entry in self.driver.get_log('performance'):
            for k, v in entry.items():
                if k == 'message' and 'status' in v:
                    msg = json.loads(v)['message']['params']
                    for mk, mv in msg.items():
                        if mk == 'response':
                            response_url = mv['url']
                            response_status = mv['status']
                            if response_url == url:
                                return response_status
