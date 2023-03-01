def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer

# 단순하게 3의 배수랑 3이 들어가는 것을 제외하려고 하기보단
# 3의 배수와 3이 들어가는 곳에서 값을 +1 해준다고 생각하는게 중요함.

print(solution(85))
