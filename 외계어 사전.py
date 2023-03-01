from itertools import permutations
def solution(spell, dic):
    answer = 2
    all_spell = list(permutations(spell, len(spell)))
    a = list()
    for i in range(len(all_spell)):
        a.append(''.join(all_spell[i]))
    for i in a:
        for j in dic:
            if i in j:
                answer = 1
    return answer

print(solution(["s", "o", "m", "d"],["moos", "dzx", "smm", "sunmmo", "som"]))

