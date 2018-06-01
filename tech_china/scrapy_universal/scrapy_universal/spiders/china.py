# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_universal.items import NewsItem


class ChinaSpider(CrawlSpider):
    name = 'china'
    allowed_domains = ['tech.china.com']
    start_urls = ['http://tech.china.com/articles/']

    rules = (
        Rule(LinkExtractor(allow=r'article/.*.html',restrict_xpaths='//div[@id="left_side"]//div[@class="con_item"]'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(.,"下一页")]')) #查看xpath中的contains
    )

    def parse_item(self, response):
        item = NewsItem()
        item['title']   = response.xpath('//h1[@id="chan_newsTitle"]//text()').extract_first()
        item['con']     = "".join(response.xpath('//div[@id="chan_newsDetail"]//p//text()').extract())
        yield item


