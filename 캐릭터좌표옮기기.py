
def solution(keyinput, board):
    start = [0 ,0]

    for i in keyinput:
        if -(board[0] - 1) / 2 <= start[0] <= (board[0] - 1) / 2 and -(board[1] - 1) / 2 <= start[1] <= (board[1] - 1) / 2:
            if i == 'left':
                if start[0] == -(board[0] - 1) / 2:
                    pass
                else: start = [start[0] - 1, start[1]]

            elif i == 'right':
                if start[0] == (board[0] - 1) / 2:
                    pass
                else: start = [start[0] + 1, start[1]]

            elif i == 'up':
                if start[1] == (board[1] - 1) / 2:
                    pass
                else: start = [start[0], start[1] + 1]

            elif i == 'down':
                if start[1] == -(board[1] - 1) / 2:
                    pass
                else: start = [start[0], start[1] - 1]

            else:
                return -1

    return start

print(solution(['down', 'down', 'down', 'down', 'down'], [7, 9]))
