T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    D = [[0]*(N) for _ in range(N)]
    D[0][0] = V[0][0]
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0: continue
            m = 987654321
            if i - 1 >= 0 and m > D[i-1][j]: m = D[i-1][j]
            if j - 1 >= 0 and m > D[i][j-1]: m = D[i][j-1]
            D[i][j] = V[i][j] + m
    print('#%d %d' %(tc, D[N-1][N-1]))