def solution(s):
    answer = 0
    l = list(s.split(' '))
    print(l)
    for i in range(len(l)):
        if l[i] == 'Z':
            answer -= int(l[i-1])
        else:
            answer += int(l[i])
    return answer

print(solution("10 Z 20 Z 1"))
