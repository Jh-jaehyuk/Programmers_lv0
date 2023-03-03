def solution(n):
    answer = []
    if n == 1:
        answer = [1]
    else:
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                if i == n//i:
                    answer.append(i)
                else:
                    answer.append(i)
                    answer.append(n//i)
    answer.sort()
    return answer

print(solution(4))
