def solution(score):
    avg = sorted([sum(i) for i in score], reverse=True)
    return [avg.index(sum(i))+1 for i in score]
print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))
