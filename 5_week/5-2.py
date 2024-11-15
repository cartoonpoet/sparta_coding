def Lis(array):
    if not array:
        return 0

    dp = [1] * len(array)

    for i in range(1, len(array)):
        for o in range(i):
            if array[o] < array[i]:
                dp[i] = max(dp[i], dp[o]+1)

    print(max(dp))

arr = [10, 9, 2, 5, 3, 7, 101, 18]
Lis(arr)
(Lis([0, 1, 0, 3, 2, 3]))
# print(Lis(arr))
# print(Lis(arr))
