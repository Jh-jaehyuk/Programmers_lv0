def solution(numbers):
    str_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i, j in zip(str_list, num_list):
        if i in numbers:
            numbers = numbers.replace(i, str(j))
    answer = int(numbers)
    return answer

#   for num, eng in enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
#       numbers = numbers.replace(eng, str(num))
#   return int(numbers)
#  enumerate 를 이용하면 영어와 숫자를 짝짓는 튜플을 작성할 수 있음.

print(solution("onefourzerosixseven"))

