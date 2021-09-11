import scrapy
from scrapy.crawler import CrawlerProcess

import re

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['localhost']
    start_urls = ['http://localhost:3000']
    """
    headers = {}
    params = {}
    
    def start_requests(self):
        yield scrapy.Requests(url, headers=headers, params=params,callback = self.parse)
    """

    def parse(self, response):
        print("procesing:"+response.url)
        orders=response.xpath("'//a[contains(@href)]'").extract()
        row_data=zip(orders)

        #Making extracted data row wise
        for item in row_data:
            #create a dictionary to store the scraped info
            scraped_info = {
                #key:value
                'page':response.url,
                'orders' : item[0]
            }
        yield scraped_info
    

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()

