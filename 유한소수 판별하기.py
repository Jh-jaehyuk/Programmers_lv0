def gcd(a, b): # 최소공배수 함수
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

def solution(a, b):
    # denom = b / gcd(a, b)
    # # numer = a / gcd(a, b)
    #
    # l = list()
    # for i in range(0, 8):
    #     for j in range(0, 4):
    #         l.append((2**i)*(5**j))
    #
    # if denom % 2 == 0 or denom % 5 == 0:
    #     if denom in l:
    #         return 1
    #     else:
    #         return 2
    # else:
    #     return 2
    # 위에 풀이는 3개의 오류가 발생함. 이유 발견 못함. 아마도 소인수 문제일 것으로 생각됨.

    b //= gcd(a, b)
    while b%2 == 0:
        b //= 2
    while b%5 == 0:
        b //= 5
    return 1 if b == 1 else 2

# 위 풀이는 인터넷에서 소인수 분해를 알아본 후 작성한 것. 오류 없음.

