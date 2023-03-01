def solution(my_string):
    a = list(''.join(my_string.split(' + ')))
    for i in a:
        answer = sum([int(i) for i in a])
    return answer

print(solution('3 + 4 + 7 + 9 + 11 + 13'))

