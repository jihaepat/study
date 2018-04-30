import json
import codecs

# file = open('test.json','r')
ttt = {456456: 123, 123: 456}
tt2 = {222: 222, 333: 333}
# file = open('ipnavi2018_04_30_11:20:52.json', 'r')
# file = open('asdf.json',a)
file_ = codecs.open('asdf.json', 'a', encoding='utf8')

# data = json.load(file)
file_.write(json.dumps(ttt))
file_.write(json.dumps(tt2))
data = json.load(open('asdf.json','r'))
print(data)
# for x in range(len(data)):
#     print(data[x].keys())

# print(data[len(data)-1]['period_number'])
