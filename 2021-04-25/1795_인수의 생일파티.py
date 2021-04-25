import sys
sys.stdin = open('input (29).txt')

def dijk(s, D, chk):
    D[s] = 0
    curV = s
    for i in range(N+1):
        minV = 1e10
        for i in range(N+1):
            if i in U: continue
            if minV > D[i]:
                minV = D[i]
                curV = i
        U.append(curV)
        # curV를 사용하여 인접한 노드의 D를 업데이트
        for i in range(1, N+1):
            if i in U: continue
            if chk == 1 and G[i][curV]:
                D[i] = min(D[i], D[curV]+G[i][curV])
            elif chk == 0 and G[curV][i]:
                D[i] = min(D[i], D[curV]+G[curV][i])

T = int(input())
for tc in range(1, T+1):
    # N개의 집, M개의 노드, 인수의 집은 X번
    N, M, X = map(int, input().split())
    G = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        # x에서 y로 가는 데 c 시간이 걸림
        x, y, c = map(int, input().split())
        # 단방향
        G[x][y] = c
    D1 = [1e10] * (N+1)
    U = []
    dijk(X, D1, 1)
    D2 = [1e10] * (N+1)
    U = []
    dijk(X, D2, 0)
    maxV = 0
    for i in range(1, N+1):
        if maxV < D1[i] + D2[i]:
            maxV = D1[i] + D2[i]

    print('#%d %d' %(tc, maxV))
