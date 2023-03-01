from math import comb
def solution(balls, share):
    answer = comb(balls, share)
    return answer

print(solution(30, 14))

# itertools 의 combinations 는 시간복잡도가 너무 높음.
# 문제가 리스트로 나오지 않는 이상 math.comb가 훨씬 빠름.
# 같은 해결법의 다른 코드도 알아둘 것!
