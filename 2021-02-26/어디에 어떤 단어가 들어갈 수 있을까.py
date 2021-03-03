T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in rangne(N):
            cnt = 0
            arr[i][j]