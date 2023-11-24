import scrapy
from  scrapy import Selector
from .items import DoubanItem
class MovieSpider(scrapy.Spider):
    name = "movie"
    describe = "hello"
    allowed_domains = ["bj.lianjia.com"]
    start_urls = []
    for i in range (1,70):
        print(i)
        url = 'https://bj.lianjia.com/zufang/dongcheng/pg'+str(i)+'/#contentList'
        print(url)
        start_urls.append(url)

    def parse(self, response):
        sel = Selector(response) 
        movie_lists = sel.xpath('//div[@class="content__list--item"]')
        print("***********!!!!!!!!")
        print(len(movie_lists))
        print("***********!!!!!!!!")
        for movie  in movie_lists:
            item = DoubanItem()
            desc = movie.xpath('normalize-space(.//p[@class="content__list--item--title"]/a/text())').get()
            pric = movie.xpath('.//span[@class="content__list--item-price"]/em/text()').get()
            ar = movie.xpath('.//p[@class="content__list--item--des"]/a/text()[1]').getall()
            m3 = movie.xpath('normalize-space(.//p[@class="content__list--item--des"]/text()[5])').get()
            floor = movie.xpath('normalize-space(.//p[@class="content__list--item--des"]/span/text()[2])').get()
            item['describe'] = desc
            item['price'] = pric 
            item['arear'] = "-".join(ar)
            item['m3'] = m3
            item['floor'] = floor
            #print(item)
            yield item
        #totalpage = sel.xpath('//div[@class="content__pg"]/@data-totalpage').get() 
        #currentpage = sel.xpath('//div[@class="content__pg"]/@data-curpage').get()
        # if currentpage>=totalpage:
        #     next_url = 'https://bj.lianjia.com/zufang/dongcheng/pg' +currentpage +'/#contentList'
        #     print(next_url)
        #     yield scrapy.Request(next_url,callback=self.parse) 
        # movelist  = response.xpath('//div[@class="item"]')
        # for movie in movelist:
        #     yield{
        #         'name':movie.xpath('.//span[@class="title"].text()').get(),
        #     } 
        
    # def parse(self, response):
    #     movelist  = response.xpath('//div[@class="item"]')
    #     for movie in movelist:
    #         yield{

    #             'name':movie.xpath('.//span[@class="title"].text()').get(),
    #             'director':movie.xpath('.//div[@class="bd"]/p/text()[1]').get(),
    #             'actors':movie.xpath('.//div[@class="bd"]/p/text()[2]').get(),
    #             'genre':movie.xpath('.//div[@class="bd"]/p/text()[3]').get(),
    #             'conntry':movie.xpath('.//div[@class="bd"]/p/text()[4]').get(),
    #             'language':movie.xpath('.//div[@class="bd"]/p/text()[5]').get(),
    #             'release_date':movie.xpath('.//div[@class="bd"]/p/text()[6]').get(),
    #             'duration':movie.xpath('.//div[@class="bd"]/p/text()[7]').get(),
    #             'rating':movie.xpath('.//span[@class="rating_num"]/text()').get(),
    #             'num_reviews':movie.xpath('.//div[@class="start"]/span[@class="rating_num"]/text()').get()
    #         }
    #     next_page = response.xpath('//*[@id="content"]/div[1]/div[2]/a[8]')
    #     if next_page:
    #         url = response.urljoin(next_page[0].get())
    #         yield scrapy.Request(url,callback=self.parse)    

