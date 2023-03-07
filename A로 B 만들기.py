from collections import Counter
def solution(before, after):
    before = Counter(before)
    after = Counter(after)
    if before - after == Counter():
        return 1
    else:
        return 0

print(solution('olleh', 'hello'))
