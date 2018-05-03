import re

regax = re.compile(r'((19|20)\w)((-|.|/|)\w)((-|.|/|)\w)')
regax2 = re.compile('[19|20]\w*[-|.|/|\w*]\w*[-|.|/|\w*]\w*')
asdf = re.compile(r'ab')
tttt = 'ab asdf'
print(asdf.findall(tttt))

ttt = '月05asdfasdf-27xcv'

print(regax2.findall(ttt))