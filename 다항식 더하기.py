def solution(polynomial):
    l = [i for i in list(polynomial.split(' ')) if i != '+']
    # l = [i for i in list(polynomial.split(' + ')]
    # 처음부터 ' + ' 로 split 하는 것이 편리함.
    number = 0
    str = 0
    for i in l:
        if 'x' in i:
            if i == 'x':
                number += 1
            elif i != 'x':
                number += int(i[:-1])
        else:
            str += int(i)

    if number == 1 and str == 0:
        answer = 'x'
    elif number == 1:
        answer = 'x' + ' + {}'.format(str)
    elif number == 0:
        answer = '{}'.format(str)
    elif str == 0:
        answer = '{}x'.format(number)
    else:
        answer = '{}x'.format(number) + ' + {}'.format(str)

    return answer

print(solution('x + x + x'))
