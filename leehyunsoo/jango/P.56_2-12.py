import http.client
from urllib.parse import urljoin, urlunparse
from urllib.request import urlretrieve
from html.parser import HTMLParser
import os


class image_parser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)

def download_image(src_url, data):
    if not os.path.exists('다운로드'):
        os.mkdir('다운로드')
    parser = image_parser()
    parser.feed(data)
    result_set = set(x for x in parser.result)

    for x in sorted(result_set):
        src = urljoin(src_url,x)
        basename = os.path.basename(src)
        target_file = os.path.join('다운로드', basename)

        print('Downloading...', src)
        urlretrieve(src, target_file)

def main():
    host = 'www.google.co.kr'

    conn = http.client.HTTPConnection(host)
    conn.request('GET','')
    resp = conn.getresponse()

    charset = resp.msg.get_content_charset()
    data = resp.read().decode(charset)
    conn.close()

    print('\n>>>>>>>>>>>>> Download Images from',host)
    url = urlunparse(('http', host, '', '', '', ''))
    download_image(url, data)

if __name__ == '__main__':
    main()