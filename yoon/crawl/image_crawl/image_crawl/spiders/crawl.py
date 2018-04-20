import scrapy

class imageCrawl(scrapy.Spider):
    name = 'image_crawl'

    def start_requests(self):
        url = ''