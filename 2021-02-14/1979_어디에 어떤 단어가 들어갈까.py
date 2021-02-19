import sys
sys.stdin = open("input (5).txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split)) for _ in range(N)]
    print(arr)
