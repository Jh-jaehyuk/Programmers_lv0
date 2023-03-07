def solution(bin1, bin2):
    ten1 = int(bin1, 2)
    ten2 = int(bin2, 2)
    a = ten1 + ten2
    answer = str(bin(a)[2:])
    return answer
