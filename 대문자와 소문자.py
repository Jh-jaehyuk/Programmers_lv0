def solution(my_string):
    l = [i for i in my_string]
    # l = [i.lower() if i.isupper() else i.upper() for i in my_string]
    # list comprehension 을 이용한 한줄 코드.
    for i in range(len(l)):
        if l[i].isupper():
            l[i] = l[i].lower()
        else:
            l[i] = l[i].upper()
    answer = ''.join(l)
    return answer

print(solution("cccCCC"))
