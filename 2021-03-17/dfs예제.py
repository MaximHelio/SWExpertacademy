def dfs(graph, v, visited):
    # 현재 노드를 방문처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i ,visited)

dfs()