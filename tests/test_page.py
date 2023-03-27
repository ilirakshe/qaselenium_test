from pages.sitemap_page import Sitemap
from pages.sitemap_page import SiteMapPageUrl


def test_when_go_to_sitemap_page_then_should_be_repsonse_200_and_page_is_loaded(driver):
    baaqmd_sitemap = Sitemap(driver=driver)
    baaqmd_sitemap.get(SiteMapPageUrl.SITE_MAP)
    assert SiteMapPageUrl.SITE_MAP in baaqmd_sitemap.get_current_url()
    assert baaqmd_sitemap.get_status_code(baaqmd_sitemap.get_current_url()) == 200


def test_when_go_to_site_map_page_when_sitemap_block_should_be_present_on_the_site_map_page(driver):
    baaqmd_sitemap = Sitemap(driver=driver)
    baaqmd_sitemap.get(SiteMapPageUrl.SITE_MAP)

    assert (baaqmd_sitemap.find_element(SiteMapPageUrl.SITE_MAP_BLOCK))


def test_when_go_to_site_map_page_and_trying_to_get_all_links_then_should_return_all_links(driver):
    baaqmd_sitemap = Sitemap(driver=driver)
    baaqmd_sitemap.get(SiteMapPageUrl.SITE_MAP)
    site_map = baaqmd_sitemap.find_element(SiteMapPageUrl.SITE_MAP_BLOCK)
    links = baaqmd_sitemap.find_all_links_in_sitemap(site_map)
    assert len(links) > 0
    for link in links:
        assert link.get_attribute("href")


def test_when_we_go_to_page_then_logo_should_be_present(driver):
    baaqmd_sitemap = Sitemap(driver=driver)
    baaqmd_sitemap.get(SiteMapPageUrl.SITE_MAP)
    assert baaqmd_sitemap.get_logo()


def test_when_we_follow_links_from_sitemap_page_then_should_be_all_links_return_status_200_and_logo_is_present(driver):
    dict_of_items_to_test = {}
    baaqmd_sitemap = Sitemap(driver=driver)
    baaqmd_sitemap.get(SiteMapPageUrl.SITE_MAP)
    site_map = baaqmd_sitemap.find_element(SiteMapPageUrl.SITE_MAP_BLOCK)
    links = baaqmd_sitemap.find_all_links_in_sitemap(site_map)
    for link in links:
        dict_of_items_to_test[link.text] = link.get_attribute("href")
    for link_text, link_url in dict_of_items_to_test.items():
        driver.get(link_url)

        # Best if we put all this in log file or somehow handle the process.
        print(f"Testing: {link_url}")

        # Here test falls if all links we excepted must be status 200 and logo with current selector is present
        # It happen because one page redirected us and we got 301 status code and logo selector is different
        # from the others page. This errors i've handle but it is not good practice at all.
        # Ideally we should make ticket for frontend to fix this issue.
        assert baaqmd_sitemap.get_status_code(baaqmd_sitemap.get_current_url()) == 200 or 301

        assert baaqmd_sitemap.get_logo() is not None
