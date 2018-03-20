import http.client as hc

body = '***filecontents***'
conn = hc.HTTPConnection('localhost',8888)
conn.request('PUT','/file',body)
respone = conn.getresponse()
print(respone.status,respone.reason)