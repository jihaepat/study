import scrapy


class QuotesSpider(scrapy.Spider):
    name = "china"
    start_url = 'http://www.gbicom.cn'

    def start_requests(self):
        # 시작시 메인 페이지의 모든 카테고리를 수집후 각각의
        # 카테고리의 url조합을 위해 start_url로 이동 및  set_category_start callback
        yield scrapy.Request(self.start_url, callback=self.set_category)
        # yield scrapy.Request(self.start_url, callback=self.crawling_data)

    # 카테고리 수집후 각각의 카테고리별 페이지 이동
    def set_category(self, response):

        category = response.xpath('//*[@id="container"]/div[2]/div/ul/li/a[@class="clearfix"]/@href').extract()
        make_category_url = [(self.start_url + category_url) for category_url in category]

        for category_url in make_category_url:
            yield scrapy.Request(url=category_url, callback=self.get_data_url)

    def get_data_url(self, response):

        data = response.xpath('//*[@id="search-contain"]/div[2]/div[1]/dl/dt/a/@href').extract()
        make_data_url = [(self.start_url + data_url) for data_url in data]

        for data_url in make_data_url:
            yield scrapy.Request(url=data_url, callback=self.crawling_data)

    def crawling_data(self, response):
        #
        # # 상표 이름
        print((response.xpath('//*[@id="brandName"]/text()').extract_first().split()))
        # # 카테고리
        # print(response.xpath('//*[@id="content_header"]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[1]/text()').extract_first())
        # # 유효기간
        # print(response.xpath('//*[@id="content_header"]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[2]/text()').extract_first())
        # # 비슷한 그룹
        # print(response.xpath('//*[@id="content_header"]/div/div[2]/div/div[1]/table/tbody/tr[3]/td/a/text()').extract())
        # # 해당프로젝트
        # print(response.xpath('//*[@id="content_header"]/div/div[2]/div/div[1]/table/tbody/tr[4]/td/a/em/text()').extract_first())
        # # 상표 ID
        # print(response.xpath('//*[@id="content_header"]/div/div[1]/div[2]/div[1]/span/em/text()').extract_first())
        #
        # yield {
        #     'brand_name':response.css('#brandName::text').extract_first(),
        #     'category':response.xpath('//*[@id="content_header"]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[1]/text()').extract_first(),
        #     'expiration date':response.xpath('//*[@id="content_header"]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[2]/text()').extract_first(),
        #     'similar_group':response.xpath('//*[@id="content_header"]/div/div[2]/div/div[1]/table/tbody/tr[3]/td/a/text()').extract(),
        #     'projectname':response.xpath('//*[@id="content_header"]/div/div[2]/div/div[1]/table/tbody/tr[4]/td/a/em/text()').extract_first(),
        #     'ID':response.xpath('//*[@id="content_header"]/div/div[1]/div[2]/div[1]/span/em/text()').extract_first()
        # }
