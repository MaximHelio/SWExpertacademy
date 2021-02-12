import sys
sys.stdin = open("input (6).txt", "r")


def mult(N, M):
    arr = []
    if N >= M:
        for i in range(N - M + 1):
            cnt = 0
            for j in range(i, i + M):
                cnt += Ai[j] * Bi[j - i]
            arr.append(cnt)
    else:
        for i in range(M - N + 1):
            cnt = 0
            for j in range(i, i + N):
                cnt += Ai[j - i] * Bi[j]
            arr.append(cnt)

    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr[-1]


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))

    print("#%d %d" %(tc, mult(N, M)))