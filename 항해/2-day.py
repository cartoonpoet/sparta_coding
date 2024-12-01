# 강에는 1번부터 ~ N번 징검다리가 차례대로 놓여있다
# 첫 징검다리는 점프해서 아무것이나 밟을 수 있다.
# 두 번쨰 점프부터는 이전에 점프한 거리보다 1이상 더 긴거리를 뛰어야함
# N번 징검다리는 반드시 밟아야한다.
T = int(input())

for i in range(T):
    N = int(input())
    start = 0
    end = N
    res = 0
    while start <= end:
        k = (start+end) // 2
        if k*(k+1) // 2 <= N:
            res = k
            start = k + 1
        else:
            end = k -1
    print(res)


