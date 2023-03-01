def solution(age):
    answer = ''
    str_age = [str(age)[i] for i in range(len(str(age)))]
    alien_age = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    # for i in range(len(str_age)):
        # answer += alien_age[int(str_age[i])] # 시간요소도 O(N^2)
    answer = ''.join([alien_age[int(str_age[i])] for i in range(len(str_age))])
        # join을 이용하는 것이 시간요소도가 더 낮을 것으로 생각됨.
    return answer

print(solution(100))

age= 23
str_age = [str(age)[i] for i in range(len(str(age)))]
print(str_age)
