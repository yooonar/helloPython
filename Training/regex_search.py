# 정규 표현식 - search
# 문장 내에 일치하는 구문이 있다면 완전한 문장이 아니어도 매칭됨

import re
p = re.compile('[a-z]+')
result1 = p.search('python')
print(result1)
# output: <re.Match object; span=(0, 6), match='python'>

result2 = p.search('3 python')
print(result2)
# output: <re.Match object; span=(2, 8), match='python'>