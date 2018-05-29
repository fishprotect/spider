#调度器，使各个模块协同工作（爬取模块+存储模块+检测模块+接口模块）
from api import app
from crawl_ip import Crawl_ip
from db import RedisClient
import setting
import time
from test_ip import Test_ip
import threading
from multiprocessing import Process
CRAWL_ENABLE = setting.CRAWL_ENABLE
TEST_ENABLE = setting.TEST_ENABLE
API_ENABLE = setting.API_ENABLE
class Manage(object):
    def __init__(self):
        self.db = RedisClient()
        self.crawl = Crawl_ip()
        self.test = Test_ip()

    def crawl_ip(self):
        print("启动爬取ip......")
        while(True):
            self.crawl.run()
            time.sleep(60)

    def test_ip(self):
        print("启动检测ip......")
        while(True):
            self.test.run()
            time.sleep(10)
    def api(self):
        print("启动接口api.....")
        app.run()

    def run(self):
        print("代理池开始运行")
        if CRAWL_ENABLE:
            t = threading.Thread(target=self.crawl_ip)
            t.setDaemon(True)
            t.start()
        if TEST_ENABLE:
             t = threading.Thread(target=self.test_ip())
             t.setDaemon(True)
             t.start()
        '''if API_ENABLE:
            api_process = Process(target=self.api)
            api_process.start()'''
if __name__ == '__main__':
    proxy_pool = Manage()
    proxy_pool.run()