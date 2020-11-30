# 정규 표현식 - findall
# 매칭되는 문자열을 리스트에 담아서 리턴해줌
import re

p = re.compile('[a-z]+')
result = p.findall('life is too short')
print(result)
# output: ['life', 'is', 'too', 'short']