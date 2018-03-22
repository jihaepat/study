import http.client as hc
import urllib.parse as ur

params = ur.urlencode({'@number' : 12524, '@type' : 'issue', '@action' : 'show'})
headers = {'Content-type' : 'application/x-www-form-urlencoded',
           'Accept' : 'text/plain'}
conn = hc.HTTPConnection('bug.pyton.org')
conn.request('POST','',params,headers)
respone = conn.getresponse()
print(respone.status, respone.reason)
data = respone.read()
print(data)
conn.close()