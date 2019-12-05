# 약수 구하기
def solution(n):
    answer = 0
    temp = []
    for i in range(1, n+1) :
        if n % i == 0 :
            temp.append(i)
    answer = sum(temp)
    return answer

    # num / 2 의 수들만 검사하면 성능 약 2배 향상
    # return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
