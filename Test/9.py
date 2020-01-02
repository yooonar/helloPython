# 문자열 내 p와 y의 개
def solution(s):
    return True if s.lower().count('p') == s.lower().count('y') else False
    # cnt_p = s.lower().count('p')
    # cnt_y = s.lower().count('y')
