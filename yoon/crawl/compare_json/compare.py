import json
from pprint import pprint

origin_file = '/home/yoonjae/study/yoon/crawl/compare_json/origin.json'

with open('origin.json') as data_file:
    data = json.load(data_file)

    # print(data[0])
    # for i in range(len(data[0])):
    #     pprint(data[0]['135001'])

    for i in data[1]['data']['publish_person'][1]:
        print(i)



