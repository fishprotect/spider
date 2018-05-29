from utils import get_page
from lxml import etree
from db import RedisClient
import random
import time
class Crawl_ip(object):
    def __init__(self):
        self.db = RedisClient()
    def ip_xici(self):
        url = 'http://www.xicidaili.com/'
        con = get_page(url)
        html = etree.HTML(con)
        ip_list = html.xpath('//tr/td[2]/text()')
        ip_port = html.xpath('//tr/td[3]/text()')
        for i in range(100):
            ip = ip_list[i] + ':' + ip_port[i]
            self.db.add(ip)
    def ip_66(self):
        preurl = 'http://www.66ip.cn/'
        for i in range(100):
            url = preurl+str(i)+'.html'
            con = get_page(url)
            if con:
                html = etree.HTML(con)
                ip_list = html.xpath('//tr')
                for i in range(2,len(ip_list)):
                    ip = ip_list[i].xpath('td[1]/text()')[0]+":"+ip_list[i].xpath('td[2]/text()')[0]
                    self.db.add(ip,10)
                intr = random.randint(5,15)
                time.sleep(intr*0.1)
    def run(self):
        self.ip_66()
        self.ip_xici()

if __name__ == '__main__':
    crawl = Crawl_ip()
    crawl.run()



