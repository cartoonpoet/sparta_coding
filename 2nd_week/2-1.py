string = input('입력: ').split(' ')

# while True:
stack = []
for i in range(len(string)):
    if string[i] in '+-*/':
        b = int(stack.pop())
        a = int(stack.pop())
        if string[i] == '+':
            stack.append(a+b)
        elif string[i] == '-':
            stack.append(a-b)
        elif string[i] == '*':
            stack.append(a*b)
        elif string[i] == '/':
            stack.append(a/b)
    else:
        stack.append(int(string[i]))


print(stack[0])