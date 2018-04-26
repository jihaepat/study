import json
import codecs

# file = open('test.json','r')
file = open('test.json','r')
# file_ = codecs.open('123456.json', 'a', encoding='utf8')

data = json.load(file)

print(len(data))
# for x in range(len(data)):
#     print(data[x].keys())

print(data[len(data)-1]['period_number'])