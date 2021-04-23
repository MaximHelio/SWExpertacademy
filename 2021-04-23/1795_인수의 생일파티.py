import sys
sys.stdin = open('input (25).txt')

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split()) # 노드수, 엣지수, 인수의집
    adj = [[0]*(N+1) for _ in range(N+1)] # 행렬처럼 풀기
    for _ in range(M):
        # x번 집에서 y번 집으로 가는 데 c시간이 걸리는 단방향 도로가 존재
        x, y, c = map(int, input().split())
        adj[x][y] = c
    V = {i for i in range(1, N+1)}
    D = dijkstra()
    D_rev = dijkstra(reverse=True)
    D_total = [D[i] + D_rev[i] for i in range(N+1)]
    D_final