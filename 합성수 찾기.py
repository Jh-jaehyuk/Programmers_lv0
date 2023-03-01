import math
def is_prime_number(n): # n이 소수인지 아닌지 판별하는 함수
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def count_prime_number(n): # n까지 소수의 개수를 세주는 함수
    prime = []
    count = 0
    for i in range(2,n+1):
        if is_prime_number(i):
            prime.append(i)
            count += 1
    return count

def solution(n):
    answer = (n - 1) - count_prime_number(n)
    return answer

print(is_prime_number(2))
print(count_prime_number(10))
print(solution(15))
