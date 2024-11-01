import math

def winningCount():
    str = input('게임 횟수, 이긴 횟수 입력: ').split(' ')
    total = int(str[0])
    winCount = int(str[1])
    winning = math.trunc((winCount / total) * 100)

    if total == winCount:
        return print(-1)

    add = 0
    while winning == (math.trunc(((winCount+add) / (total+add)) * 100)):
        add += 1
    return print(add)

winningCount()