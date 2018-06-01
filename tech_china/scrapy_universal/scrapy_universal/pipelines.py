# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
settings = get_project_settings()

class MysqlPipeline(object):
    def __init__(self):
        self.host = settings.get('MYSQL_HOST')
        self.password = settings.get('MYSQL_PASSWORD')
        self.user = settings.get('MYSQL_USER')
        self.port = settings.get('MYSQL_PORT')
        self.database = settings.get('MYSQL_DATABASE')
        self.table = settings.get('MYSQL_TABLE')
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8')
        self.cursor = self.db.cursor()
    def process_item(self,item,spider):
        print(type(item))
        data = dict(item)
        sql = 'insert into  %s (title,con) value ("%s","%s")' % (self.table,data.get('title'),data.get('con'))
        value = (item.get('title'),item.get('con'))
        self.cursor.execute(sql)
        self.db.commit()
        return item
class ScrapyUniversalPipeline(object):
    def process_item(self, item, spider):
        return item
