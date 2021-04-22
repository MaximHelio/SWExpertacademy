'''
서울(0), 천안(1), 원주(2), 논산(3), 대전(4),
대구(5), 강릉(6), 광주(7), 부산(8), 포항(9)
'''
'''
정점개수 간선개수
10 14
0 1 12
0 2 15
1 3 4
1 4 10
2 5 7
2 6 21
3 4 3
3 7 13
4 5 10
5 8 9
5 9 19
6 9 25
7 8 15
8 9 5
'''
def prim(start):
    # 시작점 설정(가중치 = 0)
    total = 0
    u = 0   # 가중치가 최소인 정점, 서울을 0으로 만들어줌
    dist[u] = 0
    # 정점의 개수만큼 반복
    for i in range(V):
        # 가중치 최소값 찾기
        min = 987654321
        for v in range(V):
            if visited[v] == 0 and min > dist[v]:
                min = dist[v]
                u = v       # 최소값이 u
        # 방문 처리
        visited[u] = 1
        total += adj[PI[u]][v]

        # 인접 정점에 업데이트 하기
        for v in range(V):
            # 인접하고 방문 안하고, 간선의 가중치 < 정점의 가중치
            if adj[u][v] != 0 and visited[v] == 0 and adj[u][v] < dist[v]:
                    dist[v] = adj[u][v] # 가중치
                    PI[v] = u
    return total

V, E = map(int, input().split()) # 정점 수, 간선 수
adj = [[0] * V for _ in range(V)] # 인접행렬
dist = [987654321] * dist        # 가중치
PI = list(range(V))  # 0 넣으면 안되는 이유? 부모(내 부모는 나야)
visited = [0] * V   # 방문체크
# 입력
for i in range(E):
    edge = list(map(int, input().split())) # 출발, 도착, 가중치
    adj[edge[0]][edge[1]] = edge[2]         # 방향성 없음
    adj[edge[1]][edge[0]] = edge[2]  # 방향성 없음

print(prim(0)):