# 간단한 메모장 만들기
# 원하는 메모를 파일에 저장하고 추가, 조회가 가능한 간단한 메모장을 만들어라.
# 필요한 기능: 메모 추가하기, 메모 조회하기
# 입력받는 값: 메모 내용, 프로그램 실행 옵션
# 출력하는 값: memo.txt
# python memo.py -a "Life is too short."

import sys
# sys.argv 의 0번째 인자: memo.py
# sys.argv 의 1번째 인자: -a
# sys.argv 의 2번째 인자: Life is too short.
option = sys.argv[1] # -a
# memo = sys.argv[2] # Life is too short. 

# print(option)
# print(memo)

# 쓰기모드
if option == '-a':
    memo = sys.argv[2] # Life is too short. 
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()

# 읽기모드
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)
