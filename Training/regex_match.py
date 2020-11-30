# 정규표현식 - match
# 문장이 찾고자하는 완전한 구문이어야만 매칭됨

import re
p = re.compile('[a-z]+')
result = p.match('python')
print(result)
# output: <re.Match object; span=(0, 6), match='python'>

nresult = p.match('3 python')
print(nresult)
# output: None