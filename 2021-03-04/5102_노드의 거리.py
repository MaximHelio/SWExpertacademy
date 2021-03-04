import sys
sys.stdin = open("sample_input (2).txt", "r")


def BFS(start):
    global cnt
    Q.append(start)
    visited[start] = 1
    while Q:
        start = Q.pop(0)
        for next in range(1, v+1):
            if node[start][next] and not visited[next]:
                Q.append(next)
                visited[next] = 1
                cnt += 1
                if next== end:
                    return cnt
    return cnt

T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    node = [[0]*(v+1) for _ in range(v+1)]
    visited = [0] * (v+1)
    for i in range(e):
        start, end = map(int, input().split())
        node[start][end] = 1
        node[end][start] = 1
    #시작노드, 도착노드
    start, end = map(int, input().split())
    Q = []
    cnt = 0
    print("#%d %d" %(tc, BFS(start)))


# def bfs(start, end):
#     global cnt
#     Q.append()
#
# T = int(input())
# for tc in ragne(1, T+1):
#     V, E = map(int, input().split())
#     node = [[0] * (V+1) for _ in range(V+1)]
#     for _ in range(E):
#         s, e = map(int, input().split())
#         node[s][e] = 1
#         node[e][s] = 1
#     start, end = map(int, input().split())
#     cnt = 0
#     bfs(start, end)
#     print("#%d %d" %())