def solution(my_string, num1, num2):
    l = [i for i in my_string]
    a = l[num1]
    b = l[num2]
    l[num2] = a
    l[num1] = b
    return ''.join(l)

print(solution("I love you", 3, 6))
