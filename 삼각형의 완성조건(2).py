def solution(sides):
    if sides == [1,2] or sides == [2,1]:
        answer = 1
    else:
        n = [i for i in range(max(sides)-min(sides)+1, max(sides)+1)]
        m = [j for j in range(max(sides)+1, sum(sides))]
        answer = len(n) + len(m)
    return answer



# def solution(sides):
#     return sum(sides) - max(sides) + min(sides) - 1
# 알고리즘의 규칙을 이용한 풀이. 깔끔하고 빠름.
# 왜 이렇게 되는지 분석 필요.


print(solution([11,7]))
