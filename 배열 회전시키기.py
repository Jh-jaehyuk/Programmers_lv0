from collections import deque
def solution(numbers, direction):
    answer = deque(numbers)
    if direction == 'right':
        # answer.appendleft(answer[-1])
        # answer.pop()
        answer.rotate(1) # 마지막 요소를 맨 앞으로 이동
    elif direction == 'left':
        # answer.append(answer[0])
        # answer.popleft()
        answer.rotate(-1) # 맨 앞 요소를 마지막으로 이동
    return list(answer)



print(solution([1,2,3], 'left'))
