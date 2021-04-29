# coding=utf-8  
import configparser
import os
from os import path

from project_path import project_path


class TestReadConfigFile(object):  
  
    def get_value(self):  
        config = configparser.ConfigParser()
        config_path = path.join(project_path, "com", "stf", "tf", "config", "config.ini")
        print(config_path)
        config.read(config_path)
        config = configparser.ConfigParser()
        # file_path = root_dir + '/config/config.ini'
        config.read(config_path)


        print(config.read(config_path))
        browser = config.get("browserType", "browserName")
  
        return(browser)  # 返回的是一个元组
  
trcf = TestReadConfigFile()  
print(trcf.get_value())   