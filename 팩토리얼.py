def factorial(n): # 팩토리얼 구하는 함수
    if n > 1:
        return n*factorial(n-1)
    else:
        return 1

def solution(n):
    i = 1
    while factorial(i) <= n:
        i += 1
    return i-1


print(solution(3628800))
