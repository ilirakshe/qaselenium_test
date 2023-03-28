# qaselenium_test

Simple pytest example for testing https://www.baaqmd.gov
Main goal is to check links from sitemap page.
We check if LOGO is present on the pages we've follow from sitemap page.
And the response from page must be "OK" or code 200.

This app uses Selenium Webdriver and you must have working Selenium Driver (ChromeDriver, FirefoxDriver etc)
In this app i allready have exported path for ChromeDriver.
But if you don't - then you must use path_to_chrome_driver in conftest.py driver method. 
* Like this :  driver = webdriver.Chrome(executable_path=r"path_to_driver",options=options, desired_capabilities=capabilities)
* Also you can just import chromedriver-binary like "pip install chromedriver-binary" and import it in 
conftest.py like "import chromedriver-binary". But notice - it is now work only with ChromeDriver. For using other drivers
code needed to slightly rewriting. Cheers.

There are some cases we have here:

1. Logo can have few css definitions
2. One page use redirect and we got not 200 code but 301 redirect
3. We use very simple Page Object patters.

This issues were handled but anyway it is not good practice.
Keep in mind what it is simplify test version. In good testing practice we will do this
on other way.



The tests run with pytest. If need please read the documentation how to run tests with this framework.