def solution(numlist, n):
    answer = sorted(numlist, key= lambda x: (abs(x-n), n-x))
    return answer

# sort(key = lambda x: (x[1], x[0])
# 2번 인덱스를 비교한 후, 1번 인덱스를 비교한 정렬
# 2번 인덱스 기준으로 오름차순으로 정리 된 후, 2번 인덱스가 같은 값일 경우
# 1번 인덱스가 더 작은 것이 앞으로 정렬

print(solution([1, 2, 3, 4, 5, 6], 4))
#(3, 3) (2, 2) (1, 1) (0, 0) (1, -1) (2, -2)
# 4 3 5 2 6 1
# 4 5 3 6 2 1
