def merge(arr1, arr2):
    return arr1 + arr2

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
mergedArray = merge(arr1, arr2)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]
    left = []
    right = []
    middle = []
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            middle.append(i)
    return quick_sort(left) + middle + quick_sort(right)


print(quick_sort(mergedArray))
