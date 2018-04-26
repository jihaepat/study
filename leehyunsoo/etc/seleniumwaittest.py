import json
import re

num_1_dict = {
    'a': 'asdf',
    'b': 'zxcv',
    'data': {}
}
num_2_dict = {

    'aa': 'asdf',
    'bb': 'zxcv',
    'ttt':[1,2,3,4]

}

# num_1_dict['data'] = num_2_dict
# print(num_1_dict)


p = (re.findall(r'(\w+)','toImg(\"1595\",\"45\",\"TMZCSQ\");')[1])
print(p)

p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m.group(1))
