def solution(dots):
    for i in dots:
        for j in range(4):
            if dots[j] != i:
                if dots[j][0] == i[0]:
                    b = abs(i[1] - dots[j][1])
                if dots[j][1] == i[1]:
                    a = abs(i[0] - dots[j][0])

    return a*b

print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))
