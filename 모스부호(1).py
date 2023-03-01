def solution(letter):
    morse = {
        '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
        '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
        '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
        '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
        '-.--': 'y', '--..': 'z'
    }
    answer = ''.join([morse[i] for i in list(letter.split(' '))])
    return answer
    # dictionary 와 join 함수 안에서의 list comprehension이 쓰인 문제

print(solution(".... . .-.. .-.. ---"))
