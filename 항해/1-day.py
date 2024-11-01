import math

str = input().split(' ')
total = int(str[0])
winCount = int(str[1])
winning = math.trunc((winCount / total) * 100)

add = 0
if total == winCount:
    add -= 1

while total != winCount and winning == (math.trunc(((winCount + add) / (total + add)) * 100)):
    add += 1
print(add)
