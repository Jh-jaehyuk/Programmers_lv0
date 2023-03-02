import math

def solution(n):
    answer = []
    div = 2
    while div <= int(math.sqrt(n)):
        if n % div == 0:
            n //= div
            if div not in answer:
                answer.append(div)
        else:
            div += 1

    if n > 1:
        answer.append(n)
    return answer

print(solution(8514))
