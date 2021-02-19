arr = [7, 2, 4, 2, 8, 2, 6, 3]
...
idx = 0
for i in range(1, len(arr)):
    if arr[idx] >= arr[i]:
        idx = i
print(idx, arr[idx])
