def solution(num, k):
    return str(num).find(str(k)) + 1 if str(k) in str(num) else -1

print(solution(str(29183), str(1)))
