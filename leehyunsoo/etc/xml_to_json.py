import csv
import json

csvfile = open('金光春_until_05.csv', 'r')
jsonfile = open('金光春_until_05.json', 'w')

fieldnames = ('publish_num', 'category_num', 'publish_date', 'trademark_name', 'person')
reader = csv.DictReader(csvfile, fieldnames)
out = json.dumps([row for row in reader], ensure_ascii=False)
print(type(out))
jsonfile.write(out)

json_file = open('金光春_until_05.json','r')
save_file = open('金光春_until_05_save.json','w')
line = json.load(json_file)
line = sorted(line, key = lambda k: k.get('publish_num', 0), reverse=True)
for x in line:
    out = json.dumps(x, ensure_ascii=False)
    save_file.write(out+',\n')


