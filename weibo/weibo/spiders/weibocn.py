# -*- coding: utf-8 -*-
import scrapy


class WeibocnSpider(scrapy.Spider):
    name = 'weibocn'
    allowed_domains = ['m.weibo.cn']
    start_urls = ['http://m.weibo.cn/']

    def parse(self, response):
        pass
