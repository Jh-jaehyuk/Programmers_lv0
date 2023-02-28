def solution(A, B):
    # str = ''
    # count = 0
    # while str == B:
    #     for i in range(count):
    #         str[i] += A[(count - 1)]
    #     for j in range(count, (len(A) - 1 - count)):
    #         str += A[j]
    #     if count > len(A):
    #         count = -1
    #         continue
    #     else:
    #         count += 1
    #         print(count)

    # answer = 0
    # new_A = ['' for i in range(len(A))]
    #
    # for i in range(len(A)): # 문자열을 한칸씩 밀어내는 부분
    #     for j in range(len(A)): # i = 0일 때는 변함없음.
    #         if i + j >= len(new_A):
    #             new_A[j + i - len(new_A)] = A[j]
    #         else:
    #             new_A[j + i] = A[j]
    #
    #     if ''.join(new_A) == B: #tmplist의 요소를 띄어쓰기 없이 이어붙임.
    #         answer = i
    #         break
    #
    # return answer
    return (B * 2).find(A)
    # 바뀐 문자열을 2배하고 그 안에서 원래 문자열이 시작하는 인덱스를 받는 함수.
    # find 함수를 잘 이용한 예시!


print(solution('atat', 'tata'))
