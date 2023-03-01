import math
def get_divisor(n): # n의 소수를 구하는 함수
    divisors = []
    length = int(math.sqrt(n)) + 1
    for i in range(1, length):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n//i)

    divisors.sort()
    return divisors

def Prime_Factorization(n): # n의 소인수를 구하는 함수
    num_list = []
    div = 2
    square = int(n**2)

    while div <= square:
        if n % div == 0:
            num_list.append(div)
            n //= div
        else:
            div += 1

    return num_list

def solution(n):
    answer = len(set(get_divisor(n)))
    return answer

print(solution(20))
