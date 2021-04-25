import sys
sys.stdin = open('input (28).txt')

def dfs(i, prob):
    global N, ans
    if prob == ans:
        return
    if i == N:
        ans = max(ans, prob)
        return
    for j in range(N):
        if not chk[j]:
            chk[j] = 1
            dfs(i+1, prob * arr[i][j])
            chk[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j] / 100
    chk = [0] * N
    ans = 0
    dfs(0, 100)
    print('#%d %.6f' %(tc, ans))
