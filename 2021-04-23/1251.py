import sys
sys.stdin = open('input (26).txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 섬의 개수
    x_list = list(map(int, input().split())) # 섬들의 x좌표
    y_list = list(map(int, input().split())) # 섬들의 y좌표
    E = float(input()) # 환경부담 세율
    Edges = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            Edges.append((i, j, (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2))

    p = [i for i in range(N + 1)]


    def findSet(v):
        if v != p[v]:
            p[v] = findSet(p[v])
        return p[v]


    Edges.sort(key=lambda x: x[2])

    ans = cnt = i = 0
    while cnt < N - 1:
        u, v, w = Edges[i]
        a, b = findSet(u), findSet(v)
        if a != b:
            p[a] = b
            ans += (w * E)
            cnt += 1
        i += 1

    print('#{} {}'.format(tc, round(ans)))