import sys
sys.stdin = open('sample_input (18).txt')

def perm(n, k, cursum): # 2 0 0
    global ans  # 987654321
    if ans < cursum:
        return
    if n == k:
        cursum += dist[t[N-1]][t[N]]
        if ans > cursum: ans = cursum
    else:
        for i in range(n):
            if visited[i+1]: continue
            t[k+1] = arr[i+1]
            visited[i+1] = True
            perm(n, k+1, cursum + dist[t[k]][t[k+1]])
            visited[i+1] = False


T = int(input())
for tc in range(1, T+1):
    ans = 987654321
    N = int(input())    # 3
    arr = list(range(N)) # 0, 1, 2
    t = [0] * N + [0]   # [0, 0, 0, 0]
    visited = [0] * N   # [0, 0, 0]
    dist = [list(map(int, input().split())) for _ in range(N)]
    # 0 18 34
    # 48 0 55
    # 18 7 0
    perm(N-1, 0, 0) # perm(2, 0, 0)
    print('#%d %d' %(tc, ans))

