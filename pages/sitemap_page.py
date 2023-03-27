from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SiteMapPageUrl:
    SITE_MAP = "/sitemap"
    SITE_MAP_BLOCK = (By.CLASS_NAME, "sitemap")
    LINKS_IN_SITE_MAP = (By.TAG_NAME, "a")


class Sitemap(BasePage):

    def find_sitemap(self):
        sitemap = self.find_element(*SiteMapPageUrl.SITE_MAP_BLOCK)

        assert SiteMapPageUrl.SITE_MAP in self.driver.current_url

        return sitemap

    def find_all_links_in_sitemap(self, parent):
        links = parent.find_elements(*SiteMapPageUrl.LINKS_IN_SITE_MAP)
        return links
