import scrapy
from time import sleep
from javascripsSpider.items import MainPageItem, DataItem

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class JSLoadTest(scrapy.Spider):
    name = "JS"
    start_url = 'http://sbgg.saic.gov.cn:9080/tmann/annInfoView/homePage.html'
    page_num = 1
    mainPageItem = MainPageItem()
    dataItem = DataItem()

    def __init__(self, *args, **kwargs):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('headless')
        self.driver = webdriver.Chrome('/home/leehyunsoo/4TB/chromedriver/chromedriver', options=chrome_options)
        super(JSLoadTest, self).__init__(*args, **kwargs)

    def start_requests(self):
        yield scrapy.Request(self.start_url, callback=self.get_main_page_url)

    def get_main_page_url(self, response):
        print('get_main_page_url')

        self.driver.get(response.url)
        sel = scrapy.Selector(text=self.driver.page_source)

        raw_url = 'http://sbgg.saic.gov.cn:9080/tmann/annInfoView/annSearch.html?annNum='
        page_num = [''.join(filter(str.isdigit, ind)) for ind in
                    sel.xpath('/html/body/div[2]/div/div/div[2]/table/tbody/tr/@onclick').extract()]
        made_url = [(raw_url + ind) for ind in page_num]

        # 기간 번호
        period_number_ar = [(''.join(ind.split())) for ind in
                            sel.xpath('/html/body/div[2]/div/div/div[2]/table/tbody/tr/td[1]/text()').extract()]

        # 공고일자
        publication_date_ar = [(''.join(ind.split())) for ind in
                               sel.xpath('/html/body/div[2]/div/div/div[2]/table/tbody/tr/td[2]/text()').extract()]
        # 이의 신청 마감일
        application_deadline_ar = [(''.join(ind.split())) for ind in
                                   sel.xpath('/html/body/div[2]/div/div/div[2]/table/tbody/tr/td[3]/text()').extract()]
        for ind in range(2):
            self.period_number = period_number_ar[ind]
            self.publication_date = publication_date_ar[ind]
            self.application_deadline = application_deadline_ar[ind]
            yield scrapy.Request(url=made_url[ind], callback=self.get_data)

    def get_data(self, response):
        # print(self.period_number, '--------', self.publication_date, '---------', self.application_deadline)
        # print(response.text)
        self.driver.get(response.url)
        # print(self.driver.)
        sleep(7)
        sel = scrapy.Selector(text=self.driver.page_source)
        total_page_num = int(''.join(
            filter(str.isdigit, (sel.xpath('//*[@id="pages"]/table/tbody/tr/td[6]/span/text()').extract_first()))))
        print(total_page_num)

        for x in range(1, 3):
            input_box = self.driver.find_element_by_class_name('pagination-num')
            input_box.clear()
            input_box.send_keys(x)
            input_box.send_keys(Keys.ENTER)
            sleep(7)

            # 상표명
            brand_name = self.driver.find_elements_by_xpath('//tr[@class="evenBj"]/td[7]')
            for x in range(len(brand_name)):
                yield {
                    # self.first_items,
                    # self.second_items
                    '기간번호': self.period_number,
                    '예비 승인 발표일': self.publication_date,
                    '이의 신청 마감': self.application_deadline,
                    '데이터': {
                        '공지 번호': '1596',
                        '발표날짜': '2018-04-20',
                        '게시판유형': '배달통지',
                        '등록번호': '29319132',
                        '신청자': '이현수',
                        '상호': '지해솔루션',
                        '상표이름' : brand_name[x].text,
                        '세부정보': {
                            '사진주소': '사진주소'
                        }
                    }

                }

        # pass

        # input_box = self.driver.find_element_by_class_name('pagination-num')
        # print(input_box.get_attribute('value'))
        # input_box.clear()
        # input_box = self.driver.find_element_by_class_name('pagination-num')
        # print(input_box.get_attribute('value'))
        # input_box.send_keys(2)
        # input_box = self.driver.find_element_by_class_name('pagination-num')
        # print(input_box.get_attribute('value'))

    # # 페이지 로딩속도로 인해 데이터 수집을 못하는 경우가 발생하여 5초가량의 waiting time 부여
    # sleep(5)
    # sel = scrapy.Selector(text=self.driver.page_source)
    #
    # # 고시 번호
    # print(sel.xpath('//tr[@class="evenBj"]/td[2]/a/text()').extract_first())
    #
    # # 상표명
    # print(sel.xpath('//tr[@class="evenBj"]/td[7]/if/text()').extract_first())
    #
    # # 공시일
    # print(sel.xpath('//tr[@class="evenBj"]/td[3]/text()').extract_first())
    #
    # # 발표타입
    # print(sel.xpath('//tr[@class="evenBj"]/td[4]/text()').extract_first())
    #
    # # 등록번호
    # print(sel.xpath('//tr[@class="evenBj"]/td[5]/text()').extract_first())
    #
    # # 신청자
    # print(sel.xpath('//tr[@class="evenBj"]/td[6]/text()').extract_first())
    #
    # # 세부 공지사항
    # print(sel.xpath('//tr[@class="evenBj"]/td[8]/a/@onclick').extract_first())

    # yield {
    #     # self.first_items,
    #     # self.second_items
    #     '기간번호': '1596',
    #     '예비 승인 발표일': '2018-04-20',
    #     '이의 신청 마감': '2018-07-20',
    #     '데이터': {
    #         '공지 번호': '1596',
    #         '발표날짜': '2018-04-20',
    #         '게시판유형': '배달통지',
    #         '등록번호': '29319132',
    #         '신청자': '이현수',
    #         '상호': '지해솔루션',
    #         '세부정보': {
    #             '사진주소': '사진주소'
    #         }
    #     }
    #
    # }
