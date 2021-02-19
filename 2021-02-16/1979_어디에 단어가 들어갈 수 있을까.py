import sys
sys.stdin = open("input (2).txt", "r")


def zigsaw(N, K, arr):
    cnt = 0
    for k in range(1, K):


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) # 5 <= N <= 15, 2 <= K <= N
    arr = [list(map(int, input().split())) for _ in range(N)]
    print("#%d %d" %(tc, zigsaw(N, K, arr)))
