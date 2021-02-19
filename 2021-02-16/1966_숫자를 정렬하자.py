def qsort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return qsort(lesser_arr) + equal_arr + qsort(greater_arr)

T  = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

