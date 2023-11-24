import pymysql
from twisted.enterprise import adbapi
from .spiders.items import DoubanItem
class ScrapymoviePipeline(object):
    def __init__(self,dbpool) -> None:
        self.dbpool = dbpool
    def process_item(self,item,spider):
        return item
    @classmethod
    def from_crawler(cls,crawler):
        params = dict(
            host = crawler.settings['MYSQL_HOST'],
            db = crawler.settings['MYSQL_DBNAME'],
            port = crawler.settings['MYSQL_PORT'],
            user = crawler.settings['MYSQL_USER'],
            passwd = crawler.settings['MYSQL_PASSWORD'],
            charset = 'utf8',
            cursorclass = pymysql.cursors.DictCursor,
            use_unicode = True
        )
        dbpool = adbapi.ConnectionPool('pymysql',**params)
        return cls(dbpool)
    def process_item(self,item,spider):
        if isinstance(item,DoubanItem):
            query = self.dbpool.runInteraction(self.do_insert,item)
            query.addErrback(self.handle_error,item,spider)
        return item    

    def do_insert(self,cursor,item):
        print("******111111****\n")
        print(item)
        print("******11111****\n")
        
        insertsql = 'insert into movie (`describe`,`price`,`m3`,`floor`,`arear`) value (%s,%s,%s,%s,%s)'
        try:
            cursor.execute(insertsql,(item['describe'],item['price'],item['m3'],item['floor'],item['arear'],))
        except BaseException as e:
            print("error****",e,"error*******")
    def handle_error(self,failue,item,spider):
        print(failue)    