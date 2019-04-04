# -*- coding: utf-8 -*-
import scrapy

from py100.items import Py100Item


class ProblemspiderSpider(scrapy.Spider):
    name = 'problemSpider'
    allowed_domains = ['http://www.runoob.com/python/']
    start_urls = []
    for i in range(61, 71):
        start_urls.append('http://www.runoob.com/python/python-exercise-example{}.html'.format(i))

    def parse(self, response):
        problems = []
        item = Py100Item()
        item['problem'] = response.xpath('//*[@id="content"]/p[2]/text()').extract()[0]
        problems.append(item)
        return problems
