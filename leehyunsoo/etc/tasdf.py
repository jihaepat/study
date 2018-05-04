dict = {
    'url': 'asdfasdf',
    'data': [
        1,2,3,4,5
    ]}

print(bool(len(dict['data'])))

import re
regax = re.compile(r'[1|2][9|0]\d\d[-|.|/|\w]\d\d[-|.|/|\w]\d\d')
num_regax = re.compile(r'\w\w\w\w\w\w\w\w')

ttt = 'asdf 2013-12-05 asdlfjklasjdfklasjdkl jaskldf masdn,mans cjah 2013-12-08'
date = max(regax.findall(ttt))
# asdf = ''.join(filter(str.isdigit,date))
print(date)