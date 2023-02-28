def solution(id_pw, db):
    # answer = ''
    # log = dict()
    # for i in range(len(db)):
    #     log[db[i][0]] = db[i][1]
    log = dict(db) # list가 key, value 쌍으로 맞출 수 있는 2개로 구성된 경우 dict(list) 변환 가능
    if id_pw[0] in log.keys():
        if id_pw[1] == log[id_pw[0]]:
            answer = 'login'
        else:
            answer = 'wrong pw'
    else:
        answer = 'fail'

    return answer

print(solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))
