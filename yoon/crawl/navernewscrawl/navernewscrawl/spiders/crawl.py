from bs4 import BeautifulSoup
import urllib.request

OUTPUT_FILE_NAME = 'output.txt'

URL = 'http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=103&oid=055'\
      '&aid=0000445667'

def get_text(URL):
    source_code_fron_URL = urllib.request.urlopen(URL)
    print(source_code_fron_URL,'!!!!!!!!!!!!!!!!')
    # soup = BeautifulSoup(source_code_fron_URL, 'lxml', from_encoding='utf-8')
    # print(soup,'!!!!!!!!!!!!!!!!!')
    # text = ''
    # for item in soup.find_all('div', id='articleBodyContents'):
    #     text = text + str(item.find_all(text=True))

    return 0
def main():
    open_output_file = open(OUTPUT_FILE_NAME, 'w')
    reslut_text = get_text(URL)
    open_output_file.write(reslut_text)
    open_output_file.close()

if __name__ == '__main__':
    main()

