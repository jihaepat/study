import re

# p = re.compile('[0-9一-龥]')

data_file = open('html.txt','r')
line = data_file.readlines()
#년도
# p = re.compile('[0-9]{4}')
#일자
p2 = re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}')

p3 = re.compile('\d+年')
# \w+月\w+日
p4 = re.compile('(19|20)\d+(-|.|/|){1}(\d)(-|.|/|){1}(\d)')
p5 = re.compile('2017')
data = '2017年01月23日'
# for x in line:
#     # for year in range(1980,2019):
#     #     p = re.compile(str(year))
#
#     if p4.match(x):
#         print('p4')
#         print(x)

if p4.findall(data):
    print('p4')
    print(data)