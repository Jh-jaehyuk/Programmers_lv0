# def solution(emergency):
#     answer = list([0 for i in range(len(emergency))])
#     l = list(enumerate(sorted(emergency, reverse=True), start=1))
#
#     for i in range(len(l)):
#         for j in range(len(emergency)):
#             if l[i][1] == emergency[j]:
#                 answer[j] = l[i][0]
#
#     return answer
# 시간복잡도에서 O(N**2)

def solution(emergency):
    answer = []
    emer_ls = {e: i + 1 for i, e in enumerate(sorted(emergency)[::-1])}
    # print(emer_ls)
    for e in emergency:
        answer.append(emer_ls[e])
        # print(answer)
    return answer
# 시간복잡도에서 유리할 것으로 생각됨

print(solution([34, 50, 21, 90, 78, 3]))

