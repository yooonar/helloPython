def solution(s):
    answer = ''
    l = len(s) # 문자열 길이 5
    if l % 2 == 0 : # 짝수
        answer = s[(l//2)-1:(l//2)+1] # str[2:3] 3
    else :
        answer = s[(l//2):(l//2)+1]

    return answer
