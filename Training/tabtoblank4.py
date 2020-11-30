# 탭을 4개의 공백으로 바꾸기
# 필요한 기능: 문서 파일 읽어들이기, 문자열 변경하기
# 입력받는 값: 탭을 포함한 문서 파일
# 출력하는 값: 탭이 공백으로 수정된 문서 파일
# python3 tabto4.py a.txt b.txt

import sys

src = sys.argv[1] # 입력
dst = sys.argv[2] # 출력

print(src)
# output: a.txt

print(dst)
# output: b.txt

f = open(src)
tab_content = f.read()
f.close()

blank_content = tab_content.replace('\t', ' '*4)
print(blank_content)

f = open('b.txt', 'w')
f.write(blank_content)
f.close()
