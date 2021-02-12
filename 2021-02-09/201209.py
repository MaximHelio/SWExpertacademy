import sys
sys.stdin = open('input (4).txt', 'r')

def dump(N, arr):
    cnt = 0
    while cnt < N:
        for i in range(len(arr) - 1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        arr[len(arr)-1] -= 1
        arr[0] += 1
        cnt +=1

    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    result = arr[len(arr)-1] - arr[0]

    return result

TC=10
for tc in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print("#%d %d" %(tc, dump(N, arr)))


# def dump(N, arr):
#     cnt = 0
#     while cnt < N:
#         for i in range(len(arr) - 1, 0, -1):
#             for j in range(i):
#                 if arr[j] > arr[j + 1]:
#                     arr[j], arr[j + 1] = arr[j + 1], arr[j]
#         arr[len(arr)-1] -= 1
#         arr[0] += 1
#         cnt +=1
#
#     result = max(arr[len(arr)-1], arr[len(arr)-2]) - min(arr[0], arr[1])
#
#     return result
#
# TC=10
# for tc in range(1, TC+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     print("#%d %d" %(tc, dump(N, arr)))
