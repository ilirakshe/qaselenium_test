import json
import logging

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)


class BasePage:

    # In a most cases best practice is to use base url in config file.
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

    def get_logo(self, url):

        logs_css = [".login-logo", ".logo-one", ".top-logo"]

        logos = max([self.driver.find_elements(By.CSS_SELECTOR, log) for log in logs_css if len(log)])
        if logos:
            return True
        else:
            logger.error(f"No such logo find element on the page: {url}")
            raise NoSuchElementException(f"No such logo element find on the page: {url}")

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
