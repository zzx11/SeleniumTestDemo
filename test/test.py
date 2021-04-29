import unittest

from com.selenium.common.browser_engine import BrowserEngine
from com.top.test.page import LoginPage


class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browserengine = BrowserEngine(cls)
        cls.driver = browserengine.open_browser(cls)

    def test_login(self):
        driver = self.driver
        driver.get("https://www.baidu.com")
        login_page = LoginPage(driver)
        login_page.search()
        driver.quit()


if __name__ == '__main__':
    unittest.main()
