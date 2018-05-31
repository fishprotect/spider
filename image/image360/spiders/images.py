# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider,Request
from urllib.parse import urlencode
from image360.items import ImageItem
import json

class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    def start_requests(self):
        data = {}
        base_url = 'http://image.so.com/zj?'
        for page in range(1,56):
            #http: // image.so.com / zj?ch = photography & sn = 60 & listtype = new & temp = 1
            data['ch'] = 'photography'
            data['sn'] = page*30
            data['listtype'] = 'new'
            data['temp'] = 1
            params = urlencode(data)
            url = base_url+params
            print(url)
            yield Request(url,self.parse)
    def parse(self, response):
        result = json.loads(response.text)
        print(type(result))
        for image in result['list']:
            item = ImageItem()
            item['id'] = image.get('imageid')
            item['url'] = image.get('qhimg_url')
            item['title'] = image.get('group_title')
            item['thumb'] = image.get('qhimg_thumb_url')
            yield item
