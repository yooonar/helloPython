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

# match 객체의 메소드 group, start, end, span

# group: 매치된 문자열 리턴
print(result.group())
# output: python

# start: 매치된 문자열의 시작 위치(인덱스) 리턴
print(result.start())
# output: 0

# end: 매치된 문자열의 끝 위치(인덱스) 리턴
print(result.end())
# output: 6

# span: 매치된 문자열의 (시작, 끝) 에 해당하는 튜플 리턴
print(result.span())
# output: (0, 6)