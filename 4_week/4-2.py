example = [(0, 6), (1, 4), (3, 5), (3, 8), (5, 7), (8, 9)]
example2 = [(1, 3), (2, 4), (5, 8), (6, 10), (8, 11), (10, 12)]

def extract_max_meeting(arr):
    answer = []

    for i in range(len(arr)-1):
        count = [arr[i]]
        for o in range(i+1, len(arr)):
            if count[len(count)-1][1] < arr[o][0]:
                count.append(arr[o])
        answer.append(len(count))
    return max(answer)

print(extract_max_meeting(example))
print(extract_max_meeting(example2))