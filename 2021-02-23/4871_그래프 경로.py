#인접 행렬, 인접 리스트 만들 줄 알아야 dfs, bfs 할 수 있음
# 그래프 입력
import sys
sys.stdin = open("sample_input (1).txt", "r")


def dfs(node):
    visited[node] = False
    for i in graph[node]:
        if visited[i]:
            dfs(i)

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [True for _ in range(V + 1)]
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        # print(graph)
    start, end = map(int, input().split())
    # 시작노드부터 dfs를 시작.
    dfs(start)
    result = 1
    # 0으로 결과를 바꾼다.
    if visited[end]:
        result = 0
    print("#%d %d" % (tc, result))


# 1 4 # 단방향
# 1 3
# 2 3
# 2 5
# 4 6
#
#
# G = [[], [3, 4], [3, 5], [], [6], [], []]
# GR = [[0, 0, 0, 0, 0, 0, 0],
#       [0, 0, 0, 1, 1, 0, 0],
#       [0, 0, 0, 1, 0, 1, 0]
#       ...]
# a, b = map(int, input().split())
# G[a].append(b)
# GR[a][b] = 1
#
# 양방향일 때
# G[a].append(b)
# G[b].append(a)
#
# GR[a][b] = 1
# GR[b][a] = 1
#
# def dfs(v):
#     ST = []
#     visited = [False] * (V+1)
#     ST.append(v)
#     visited[v] = True
#     while ST:
#         v = ST.pop(-1)
#         print(v)
#         # if v == GOAL:
#         #     return 1
#         for w in G[v]:
#             if not visited[w]:
#                 ST.append(w)
#                 visited[w] = True
#                 if w == GOAL:
#                     return 1
#     return 0
#
# def dfsr(v):
#     print(v)
#     visited[v] =True

