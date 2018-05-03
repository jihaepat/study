import re

regax = re.compile(r'((19|20)\w)((-|.|/|)\w)((-|.|/|)\w)')
regax2 = re.compile(r'[1|2][9|0]\d*[-|.|/|\w]\d\d[-|.|/|\w]\d\d')
asdf = re.compile(r'ab')
tttt = 'ab asdf'
print(asdf.findall(tttt))

ttt = '   2013-05-27'

print(regax2.findall(ttt))