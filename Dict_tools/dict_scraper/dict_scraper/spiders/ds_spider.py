# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from dict_scraper.items import DictScraperItem

class DictSpider(CrawlSpider):
#class DictSpider(scrapy.spider):
    name = 'dict'

    allowed_domains = ['uighurdictionary.com']
    start_urls = ['http://www.uighurdictionary.com/draconian/']

    rules = [
        Rule(LinkExtractor(
            allow=['[a-zA-Z]*']),
            callback='parse_page',
            follow=True),
    ]

    def parse_page(self, response):        
        item = DictScraperItem()
        item['url'] = response.url
        item['category'] = response.xpath("/html/body/div[1]/div/div/div/div[1]/div/main/article/div/div/i[1]").extract()

        item['entry_eng'] = response.url.split('/')[-2]
        item['entry_ug_ar'] = response.xpath("//div[@class='entry-content']/span[@class='def-ug-ar']/text()").extract()
#        item['entry_ug'] = response.xpath("//div[@class='entry-content']/span[@class='def-ug']/text()").extract()
        item['entry_ug'] = response.xpath("/html/body/div[1]/div/div/div/div[1]/div/main/article/div/div/span[2]/text()").extract()
        next_url = response.xpath("//div[@class='nav-next']/@href").extract()



        yield item

#def main():
#    process = CrawlerProcess()
#    process.crawl(Dict_spider)
#    process.start()


#if __name__ == '__main__':
#    main()