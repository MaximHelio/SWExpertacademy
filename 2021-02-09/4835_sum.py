import sys
sys.stdin = open('sample_input (1).txt', 'r')

T= int(input())
for tc in range(1, T+1):
    N, M= map(int, input().split())
    Ai = list(map(int, input().split()))

    total = 0
    arr = []
    k = 0

    while k <= len(Ai)-M:
        total = 0
        for l in range(k, k+M):
            total += Ai[l]
        k += 1
        arr.append(total)
    print(arr)
# 정렬
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)

    total_min = arr[0]
    total_max = arr[len(arr)-1]

    result = total_max - total_min
    print("#%d %d" %(tc, result))