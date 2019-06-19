# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class DictScraperItem(Item):
    url = Field()
    category = Field()
    entry_eng = Field()
    entry_ug_ar = Field()
    entry_ug = Field()