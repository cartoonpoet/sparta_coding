string = input('입력: ')

used={}
start = end = 0

for i, char in enumerate(string):
    if char in used and start <= used[char]:
        start = used[char] + 1
    else:
        end = max(end, i-start+1)
    used[char] = i

print(start, end, used)