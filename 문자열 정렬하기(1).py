def solution(my_string):
    # l = [int(i) for i in my_string if i in list([str(j) for j in range(10)])]
    l = [int(i) for i in my_string if i.isdigit()]
    # isdigit() 함수는 값이 숫자인지 아닌지를 판별해주는 함수
    answer = list(sorted(l))
    return answer

print(solution("abcde0"))
