import urllib.request
from html.parser import HTMLParser


class image_parser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)

def parse_image(data):
    parser = image_parser()
    parser.feed(data)
    data_set = set(x for x in parser.result)
    print('\n'.join(sorted(data_set)))

def main():
    url = 'http://www.google.co.kr'

    f = urllib.request.urlopen(url)
    charset = f.headers.get_content_charset()
    #         charset = f.info().getparams('charset')
    data = f.read().decode(charset)
    f.close()

    print('\n>>>>>>>>>>> Fetch Images from', url)
    parse_image(data)

if __name__ == '__main__':
    main()