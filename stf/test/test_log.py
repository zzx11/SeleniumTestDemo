# __author:zhaozhixiang  
# data:2021/4/29
import time

from com.selenium.common import Logger

mylogger = Logger(logger='TestMyLog').getlog()


class TestMyLog(object):

    def print_log(self):
        mylogger.info("打开浏览器")
        mylogger.info("最大化浏览器窗口。")

        mylogger.info("打开百度首页。")
        time.sleep(1)
        mylogger.info("暂停一秒。")
        mylogger.info("关闭并退出浏览器。")


testlog = TestMyLog()
testlog.print_log()