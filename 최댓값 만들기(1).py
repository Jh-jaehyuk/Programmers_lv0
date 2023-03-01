def solution(numbers):
    numbers.sort()
    # n = max(numbers)
    # numbers.pop()
    # m = max(numbers)
    # answer = n * m
    answer = numbers[-1] * numbers[-2] 
    # pop 이용하지말고 인덱스를 생각하면 더 간단함
    return answer

print(solution([0, 31, 24, 10, 1, 9]))

