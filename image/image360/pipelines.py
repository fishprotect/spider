# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
settings = get_project_settings()

class MysqlPipeline():
    def __init__(self):
        self.host       =  settings.get('MYSQL_HOST')
        self.password   =  settings.get('MYSQL_PASSWORD')
        self.user       =  settings.get('MYSQL_USER')
        self.port       =  settings.get('MYSQL_PORT')
        self.database   =  settings.get('MYSQL_DATABASE')
        self.db         =  pymysql.connect(self.host,self.user,self.password,self.database,charset = 'utf8')
        self.cursor     =  self.db.cursor()
    def process_item(self,item,spider):
        data = dict(item)
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql = "INSERT INTO images (%s) value (%s)" %(keys,values)
        self.cursor.execute(sql,tuple(data.values()))
        self.db.commit()
        return item

class ImagePipeline(ImagesPipeline):
    def file_path(self,request,response = None,info = None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok,x in results if ok]
        if not image_paths:
            raise DropItem
        return item
    def get_media_requests(self, item, info):
        yield Request(item['url'])


class Image360Pipeline(object):
    def process_item(self, item, spider):
        return item
