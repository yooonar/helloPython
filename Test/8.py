# 문자열 내마음대로 정렬하기
def solution(strings, n):
    strings.sort()
    return sorted(strings, key = lambda strings : strings[n])
