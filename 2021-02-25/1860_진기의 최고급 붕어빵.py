import sys
sys.stdin = open("input (1).txt", "r")

def fishbread(N, M, K, arr):
    arr.sort()
    if N > K:
        for i in range(N):
            if arr[i] < int(i // K + 1)  * M:
                return "Impossible"
        return "Possible"


    else:
        for i in range(N):
            if arr[i] < M:
                return "Impossible"
        return "Possible"


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split())) # 총 N명
    print("#%d %s" % (tc, fishbread(N, M, K, arr)))