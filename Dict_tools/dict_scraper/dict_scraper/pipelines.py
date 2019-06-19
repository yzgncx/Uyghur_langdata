# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
from scrapy.exporters import CsvItemExporter
import csv


class DictScraperPipeline(object):
    return item
#    def process_item(self, item, spider):
 #       required_fields = [
  #              'url',
   #             'category',
    #            'entry_eng',
     #           'entry_ug_ar',
      #          'entry_ug',
       #     ]
        #if all(field in item for field in required_fields):
         #   return item
        #else:
         #   raise DropItem("excluded bad data")


class CSVPipeline(object):
    def __init__(self, path):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        file = open('%s_items.csv' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = CsvItemExporter(file)
        self.exporter.fields_to_export = [
                'url',
                'category',
                'entry_eng',
                'entry_ug_ar',
                'entry_ug',
            ]
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
