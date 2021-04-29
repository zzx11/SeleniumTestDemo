import logging
import time
from os import path
from project_path import project_path


class Logger(object):

    def __init__(self, logger):
        # 命名log文件
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H', time.localtime(time.time()))
        log_path = path.join(project_path, "com", "report", "logs", "")
        log_name = log_path + rq + '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台  
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式  
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler  
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger
