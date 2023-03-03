# def solution(array, n):
#     l = sorted([(i-n, abs(i-n)) for i in array], key=lambda x:(x[1], x[0]))
#     answer = n + l[0][0]
#     return answer

def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n))
    answer = array[0]
    return answer
# 이렇게 풀이하면 array의 요소를 바꾸지 않고 정렬하므로 0번째 인덱스 값을 불러오기만 하면 해결.

print(solution([9,11,12], 10))
print(solution([15,11,13], 14))

