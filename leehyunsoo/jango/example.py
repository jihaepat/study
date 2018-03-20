import re


def function1(x):
    return '*'.join(x.group(2)) if x.group(2) else '-'.join(x.group(3))


print(re.sub(r'(([02468]{2,})|([13579]{2,}))', function1, '11112222'))

print( re.sub(r'(([02468]{2,})|([13579]{2,}))', function1, '11112222'))
