# 정규 표현식 - finditer
# iterator object 형식으로 리턴됨

import re
p = re.compile('[a-z]+')
result = p.finditer('life is too short')

print(result)
# output: <callable_iterator object at 0x106946278>

for r in result :
    print(r)
# <re.Match object; span=(0, 4), match='life'>
# <re.Match object; span=(5, 7), match='is'>
# <re.Match object; span=(8, 11), match='too'>
# <re.Match object; span=(12, 17), match='short'>