# 문자열 다루기 기본
def solution(s):
    return True if s.isdigit() == True and (len(s) == 4 or len(s) == 6) else False
# 다른 방법
# answer = False
# types = s.isdigit()
# if types == True and (len(s) == 4 or len(s) == 6) :
#     answer = True
# return answer
