import random
import time
from utils import get_page,random_time
import threading
import setting
from db import RedisClient
import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
test_url = setting.TEST_URL

class Test_ip(object):
    def __init__(self):
        self.db = RedisClient()
        self.headers = headers
        self.url = test_url
    def get_url(self,proxy):
        try:
            con =  requests.get(self.url,headers = self.headers,proxies = proxy)
            if con.status_code==200:
                return True
            else:
                return False
        except:
            return False
    def test(self,ip):
        ip = ip.decode('utf-8')
        proxy = {'http':'http://'+ip}
        test_result = self.get_url(proxy)
        if test_result:
            self.db.max(ip,)
        else:
            self.db.decrease(ip)
    def run(self):
        proxies = self.db.all()
        for i in range(len(proxies)):
            ip = proxies[i]
            t = threading.Thread(target=self.test,args=(ip,))
            t.setDaemon(True)
            t.start()
            random_time()
            if i%100==0:
                time.sleep(5)
if __name__=='__main__':
    test = Test_ip()
    test.run()






