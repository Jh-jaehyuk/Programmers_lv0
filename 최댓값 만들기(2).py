from itertools import combinations
def solution(numbers):
    num_list = list(combinations(numbers, 2))
    answer = [num_list[i][0] * num_list[i][1] for i in range(len(num_list))]
    return max(answer)
