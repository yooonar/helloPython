# 정규표현식 - match

import re
p = re.compile('[a-z]+')
result = p.match('python')
print(result)
# output: <re.Match object; span=(0, 6), match='python'>

nresult = p.match('3 python')
print(nresult)
# output: None