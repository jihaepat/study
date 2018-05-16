import json

#
# with open('broker_name.json') as data_file:
#     data = json.load(data_file)
#
# print(data)

file = open('broker_name.json', 'r', encoding='utf8')
#
data = json.load(file)

print(data[0:]['name'])
