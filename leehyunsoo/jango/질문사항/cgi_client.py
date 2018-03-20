import urllib.request, urllib.parse, urllib.error
from urllib.parse import urlencode


url = 'http://localhost:8888/work/study_jango/study/leehyunsoo/jango/cgi-bin/script.py'
data = {
    'language' : 'python',
    'framework' : 'django',
    'email' : 'lhs950204@naver.com'
}

enc_data = urlencode(data)
enc_data = enc_data.encode('utf-8')
f = urllib.request.urlopen(url, enc_data)	# POST
print((f.read()))