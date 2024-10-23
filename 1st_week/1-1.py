# 문자열 팰린드롬 여부 확인

string = input('예시 입력: ')

reverseString = ''
for s in reversed(range(len(string))):
    reverseString += string[s]

print(reverseString == string)