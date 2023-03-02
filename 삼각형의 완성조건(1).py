def solution(sides):
    answer = list(sorted(sides))
    return 1 if (answer[0] + answer[1]) > max(sides) else 2

print(solution([1,2,3]))

