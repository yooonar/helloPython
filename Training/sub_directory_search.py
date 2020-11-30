# 하위 디렉토리 검색하기
# 특정 디렉토리부터 시작해서 그 하위 모든 파일 중 파이썬 파일(*.py) 만 출력해주는 프로그램을 만들어라.

import os

def search(dirname) :
    try:
        # 전체 파일 이름
        filenames = os.listdir(dirname)

        for filename in filenames :
            # dirname == 입력받은 값 == /Users/yoonar/Documents/study/helloPython/Training
            # filename == 해당 경로의 모든 파일 이름
            full_filename = os.path.join(dirname, filename)
            # print(full_filename) # 전체 파일 경로
            # output: /Users/yoonar/Documents/study/helloPython/Training/gugu.py

            ext = os.path.splitext(full_filename)
            # print(ext) # 확장자 추출하기 위해 문자열 자르기
            # output: ('/Users/yoonar/Documents/study/helloPython/Training/gugu', '.py')

            # full_filename 이 파일이 아니라 디렉토리라면? 재귀함수로 다시 호출함
            if os.path.isdir(full_filename) :
                search(full_filename)

            # full_filename 이 파일이라면?
            else :
                if ext[-1] == '.py' : # 맨 끝에 있는 확장자가 .py 이냐?
                    print(full_filename)

    except PermissionError :
        # 퍼미션 오류나도 오류메시지 안나오도록 패스
        pass

search("/Users/yoonar/Documents/study/helloPython/Training")