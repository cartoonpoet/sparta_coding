x, y = map(int, input().split())
z = (y * 100) // x

if z > 98:
    print(-1)
else:
    start = 0
    end = x
    # print('start:', start, ' end:', end)
    while start < end:
        mid = (start + end) // 2
        new_z = ((y + mid) * 100) // (x + mid)
        # print('mid: ', mid, 'new_z:', new_z)
        if new_z > z:
            end = mid
        else:
            start = mid + 1
        # print('start:', start, ' end:', end)
    mid = (start + end) // 2
    print(mid)
