import sys
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
TARGET_URL_BEFORE_PAGE_NUM = 'http://news.donga.com/search?p='
TARGET_URL_BEFORE_KEWORD = '&query='
TARGET_URL_REST = '&check_news=1&more=1&sorting=3&search_date=1&v1=&v2=&range=3'

def get_link_from_news_title(page_num, URL, output_file):
    for i in range(page_num):
        current_page_num = 1 + i*15
        position = URL.index('=')
        URL_with_page_num = URL[: position + 1] + str(current_page_num) \
                            + URL[position + 1:]
        print(URL_with_page_num , '!!!!!!!!!!')
        source_code_from_URL = urllib.request.urlopen(URL_with_page_num)
        soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')

        for title in soup.find_all('p', 'tit'):
            title_link = title.select('a')

            article_URL = title_link[0]['href']
            get_text(article_URL, output_file)
def get_text(URL, output_file):
    source_code_from_url = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_url, 'lxml', from_encoding='utf-8')
    content_of_article = soup.select('div.article_txt')
    print(content_of_article)
    for item in content_of_article:
        string_item = str(item.find_all(text=True))
        output_file.write(string_item)

def main(argv):
    if len(argv) != 4:
        print('python [모듈이름] [키워드] [가져올 페이지 숫자] [결과 파일명]')
        return
    keyword = argv[1]
    page_num = int(argv[2])
    output_file_name = argv[3]
    target_URL = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_KEWORD \
                +quote(keyword) + TARGET_URL_REST
    output_file = open(output_file_name, 'w')
    get_link_from_news_title(page_num, target_URL, output_file)
    output_file.close()

if __name__ == '__main__':
    main(sys.argv)
