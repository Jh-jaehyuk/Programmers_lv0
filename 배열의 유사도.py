def solution(s1, s2):
    answer = 0
    for i in s1:
        if i in s2:
            answer += 1
    return answer

#   return len(set(s1) & set(s2))
#   교집합을 이용한 풀이. 매우 간략함.
print(solution(['a','b','c'], ['com', 'b', 'd', 'p', 'c']))
