# qaselenium_test

Simple pytest example for testing https://www.baaqmd.gov
Main goal is to check links from sitemap page.
We check if LOGO is present on the pages we've follow from sitemap page.
And the response from page must be "OK" or code 200.

There are some cases we have here:

1. Logo can have few css definitions
2. One page use redirect and we got not 200 code but 301 redirect
3. We use very simple Page Object patters.

This issues were handled but anyway it is not good practice.
Keep in mind what it is simplify test version. In good testing practice we will do this
on other way.

The tests run with pytest. If need please read the documentation how to run tests with this framework.