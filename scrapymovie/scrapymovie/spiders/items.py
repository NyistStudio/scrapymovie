import scrapy
class DoubanItem(scrapy.Item):
    describe = scrapy.Field()
    price = scrapy.Field()
    arear = scrapy.Field()
    floor = scrapy.Field()
    m3 = scrapy.Field()
