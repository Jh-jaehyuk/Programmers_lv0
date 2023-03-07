def solution(my_string):
    answer = []
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, ' ')
    l = my_string.split(' ')
    for i in l:
        if i != '':
            answer.append(int(i))
    return sum(answer)

print(solution("aAb1B2cC34oOp"))
