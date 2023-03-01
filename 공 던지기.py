def solution(numbers, k):
    answer = numbers[(2*(k-1)%len(numbers))]
    return answer
# input, output을 보고 규칙을 파악하면 쉬움
print(solution([1,2,3], 3))
