def solution(num_list, n):
    answer = []
    for i in range(0 ,len(num_list), n): # 0~len(num_list)까지 n간격만큼
        answer.append(num_list[i:i+n]) # i = 0, 2, 4, 6
    return answer
# 규칙을 찾아내야 쉬운 문제
print(solution([1,2,3,4,5,6,7,8], 2))

