import http.client as hc
conn = hc.HTTPConnection('www.example.com')
conn.request('HEAD','/index.html')
res = conn.getresponse()
print(res.status, res.reason)
data = res.read()
print(len(data))
data == ''