# 게시판 페이징
# 게시물의 총 건수와 한 페이지에 보여줄 게시물의 수를 입력으로 주었을 때 총 페이지를 출력
# 함수 이름: GetTotalPage
# 입력받는 값: 게시물의 총 건수 == m, 한 페이지에 보여줄 게시물의 수 == n
# 출력하는 값: 총 페이지의 수

def GetTotalPage(m, n):
    # 나누어 떨어지면 +1 하지 않음
    if m % n == 0 :
        # m 을 n으로 나눈 몫 == //
        return m // n 
    else :
        return m // n + 1

print(GetTotalPage(5, 10))
# output: 1
print(GetTotalPage(15, 10))
# output: 2
print(GetTotalPage(25, 10))
# output: 3
print(GetTotalPage(30, 10))
# output: 3