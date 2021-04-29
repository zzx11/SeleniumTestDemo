import configparser
from os import path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from project_path import project_path
from com.selenium.common import Logger

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):
    chrome_driver_path = path.join(project_path, "chromedriver.exe")

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        config = configparser.ConfigParser()
        config_path = path.join(project_path, "com", "stf", "tf", "config", "config.ini")
        print(config_path)
        config.read(config_path)
        browser = config.get("browserType", "browserName")
        logger.info("选择%s 浏览器" % browser)
        """
        通过if语句，来控制初始化不同浏览器的启动，默认是启动Chrome
        :return: driver
        """
        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("启动 firefox 浏览器.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("启动 Chrome 浏览器.")
        elif browser == "IE":
            driver = webdriver.Ie()
            logger.info("启动 IE 浏览器.")
        elif browser == "ChromeHeadless":
            options = Options()
            # # root权限赋予
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('blink-settings=imagesEnabled=false')
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')  # 允许在无GPU的环境下运行，可选
            # options.add_argument('--window-size=1920x1080')  # 建议设置 chrome_options=options
            driver = webdriver.Chrome(self.chrome_driver_path, chrome_options=options)
            logger.info("启用chrome浏览器，无头模式.")

        driver.maximize_window()
        logger.info("最大化浏览器窗口.")
        driver.implicitly_wait(60)
        logger.info("隐式等待10s.")
        return driver

    def quit_browser(self):
        logger.info("执行结束，关闭浏览器.")
        self.driver.quit()
