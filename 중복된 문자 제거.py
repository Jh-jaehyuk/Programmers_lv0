def solution(my_string):
    answer = ''.join([my_string[i] for i in range(len(my_string)) if my_string[i] not in my_string[:i]])
    return answer

print(solution("We are the world"))
