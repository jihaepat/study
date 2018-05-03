ar = ['1','2','3','1']
ttt={'a':'1'}
ar2= []

url = 'https://www.baidu.com/s?wd=asic&pn=100&gpc=stf%3D1525186800%2C1525359598%7Cstftype%3D2'
url2 = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=asic&oq=asic&rsv_pq=b31fc32f00035ad6&rsv_t=477bEh8oeb9TKg8%2FFid7cFM75fa%2B5ikRnrSxOwduNo7YzI3myW4BHlvE0kM&rqlang=cn&rsv_enter=1&gpc=stf%3D1525100400%2C1525359598%7Cstftype%3D2&tfflag=1&rsv_srlang=cn&sl_lang=cn&rsv_rq=cn'
ttt = url2.split('&')

print(ttt)
for x in ttt:
    if 'gpc' in x:
        print(x)