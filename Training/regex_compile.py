# 정규 표현식 - compile 옵션 종류들
import re

print("---------------------")
print("\n1. DOTALL\n")
# 1-1. 줄바꿈 문자열이 있는 경우
dotall1 = re.compile('a.b')
dotall_result1 = dotall1.match('a\nb')
print(" 1-1. compile(a.b) -> match(a\\nb) :\n ", dotall_result1)
# output: None

# 1-2. 줄바꿈 문자열이 있는 경우 매칭 방법 - DOTALL
dotall2 = re.compile('[a-z]+', re.DOTALL)
dotall_result2 = dotall2.match('a\nb')
print("\n 1-2. compile('[a-z]+', re.DOTALL) -> match('a\\nb') :\n ", dotall_result2)
# output: <re.Match object; span=(0, 1), match='a'>

# 1-3. 줄바꿈 문자열이 있는 경우 매칭 방법 - DOTALL 의 약어 S
dotall3 = re.compile('[a-z]+', re.S)
dotall_result3 = dotall3.match('a\nb')
print("\n 1-3. compile('[a-z]+', re.S) -> match('a\\nb') :\n ", dotall_result3)
# output: <re.Match object; span=(0, 1), match='a'>

print("\n---------------------")
print("\n2. IGNORECASE\n")
# 2-1. 대소문자를 구분하는 문자열이 있는 경우
ignorecase1 = re.compile('[a-z]')
print(" 2-1. compile('[a-z]') -> match('python') :\n ", ignorecase1.match('python'))
# output: <re.Match object; span=(0, 1), match='p'>
print("\n 2-1. compile('[a-z]') -> match('Python') :\n ", ignorecase1.match('Python'))
# output: None
print("\n 2-1. compile('[a-z]') -> match('PYTHON') :\n ", ignorecase1.match('PYTHON'))
# output: None

# 2-2. 대소문자를 구분하는 문자열이 있는 경우 - IGNORECASE
ignorecase2 = re.compile('[a-z]', re.IGNORECASE)
print("\n 2-2. compile('[a-z]', re.IGNORECASE) -> match('python') :\n ", ignorecase2.match('python'))
# output: <re.Match object; span=(0, 1), match='p'>
print("\n 2-2. compile('[a-z]', re.IGNORECASE) -> match('Python') :\n ", ignorecase2.match('Python'))
# output: <re.Match object; span=(0, 1), match='P'>
print("\n 2-2. compile('[a-z]', re.IGNORECASE) -> match('PYTHON') :\n ", ignorecase2.match('PYTHON'))
# output: <re.Match object; span=(0, 1), match='P'>

# 2-3. 대소문자를 구분하는 문자열이 있는 경우 - IGNORECASE 의 약어 I
ignorecase3 = re.compile('[a-z]', re.I)
print("\n 2-3. compile('[a-z]', re.I) -> match('python') :\n ", ignorecase3.match('python'))
# output: <re.Match object; span=(0, 1), match='p'>
print("\n 2-3. compile('[a-z]', re.I) -> match('Python') :\n ", ignorecase3.match('Python'))
# output: <re.Match object; span=(0, 1), match='P'>
print("\n 2-3. compile('[a-z]', re.I) -> match('PYTHON') :\n ", ignorecase3.match('PYTHON'))
# output: <re.Match object; span=(0, 1), match='P'>


print("\n---------------------")
print("\n3. MULTILINE\n")

data = """python one
life is too short
python two
you need python
python three"""
# ^python\s\w+ : 맨 처음(^) 에 python 이라는 글자가 나오고 공백(\s) 이 나오고 그 다음 알파벳 | 숫자 | _ 중의 한 문자(\w)가 1개 이상 반복되는 것

# 3-1. 여러줄 중 맨 처음 나오는 문자열을 매칭하려는 경우
multiline1 = re.compile('^python\s\w+')
print(" 3-1. ('^python\s\w+') -> findall(data) :\n ", multiline1.findall(data))
# output: ['python one']

# 3-2. 여러줄 중 맨 처음 나오는 문자열을 매칭하려는 경우 - MULTILINE
multiline2 = re.compile('^python\s\w+', re.MULTILINE)
print("\n 3-2. ('^python\s\w+', re.MULTILINE) -> findall(data) :\n ", multiline2.findall(data))
# output: ['python one', 'python two', 'python three']

# 3-3. 여러줄 중 맨 처음 나오는 문자열을 매칭하려는 경우 - MULTILINE 의 약어 M
multiline3 = re.compile('^python\s\w+', re.M)
print("\n 3-3. ('^python\s\w+', re.M) -> findall(data) :\n ", multiline3.findall(data))
# output: ['python one', 'python two', 'python three']
