# def solution(hp):
#     n1 = 0
#     n3 = 0
#     n5 = 0
#     if hp % 5 == 0:
#         n5 += hp // 5
#     else:
#         n5 += hp // 5
#         if (hp % 5) % 3 == 0:
#             n3 += (hp % 5) // 3
#         else:
#             n3 += (hp % 5) // 3
#             n1 += (hp % 5) % 3
#
#     answer = n1 + n3 + n5
#     return answer

def solution(hp):
    return (hp // 5) + (hp % 5 // 3) + (((hp % 5)) % 3)

print(solution(999))
