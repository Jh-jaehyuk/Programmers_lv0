def solution(rsp):
    d = dict()
    d['2'] = '0'
    d['5'] = '2'
    d['0'] = '5'

    answer = ''.join([d[rsp[i]] for i in range(len(rsp))])
    return answer

print(solution('205'))

a = ''
rsp = '205'
d = {'0':'5', '2':'0', '5':'2'}
for i in rsp: # 대상이 문자열일 경우 for 구문 돌릴시 rsp[i]로 인식됨.
    print(d[i])

