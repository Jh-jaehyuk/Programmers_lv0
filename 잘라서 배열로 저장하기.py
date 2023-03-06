import math
def solution(my_str, n):
    answer = []
    for i in range(math.ceil(len(my_str)/n)):
        if n * (i+1) <= len(my_str):
            answer.append(my_str[n*i:n*(i+1)])
        else:
            answer.append(my_str[n*i:])
    return answer
# 인덱스가 초과하는 경우를 고려하여 if문을 설정했는데...

print(solution("abcdef123", 3))

# def solution(my_str, n):
#     return [my_str[i: i + n] for i in range(0, len(my_str), n)]
# 슬라이싱은 인덱스를 초과해도 에러가 나지 않음!
