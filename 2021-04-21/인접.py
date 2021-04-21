'''
5 6
1 2 1 3 3 2 3 4 2 5 5 4
'''
V, E = map(int, input().split())
edge = list(map(int, input().split()))
adj = [[0]*(V+1) for _ in range(V+1)]
adj_list = [[] for _ in range(V+1)]
for i in range(E):
    n1 = edge[i*2]
    n2 = edge[i*2+1]
    adj[n1][n2] = 1 # 인접
    # adj[n2][n1] = 1 # 무향 그래프인 경우 대칭

    adj_list[n1].append(n2)
    # adj_list[n2].append(n1) # 무향인 경우에만

for i in range(1, V+1): # i에 인접인 노드
    for j in range(1, V+1):
        if adj[i][j]: # 인접행렬인 경우
            print(i, j)
    for j in adj_list[i]:
        print(i, j)