# 방향 그래프가 주어지면 1번 정점에서 N번 정점으로 가는 모든
# 경로의 가지수를 출력하는 프로그램을 작성하시오.
# 아래 그래프에서 1번 정점에서 5번 정점으로 가는 가지수는
# 1 2 3 4 5
# 1 2 5
# 1 3 4 2 5
# 1 3 4 5
# 1 4 2 5
# 1 4 5
# 총 6가지이다.

def dfs(v):
    global cnt
    if v == n: # 종착지점이라면(5에 도착했다면)
        cnt += 1
        # for x in path:
        #     print(x, end=' ')
        # print()
    else: # 아니라면 가지가 뻗어야 함
        for i in range(1, n+1): # 방문하려는 노드 번호
            if g[v][i] == 1 and chk[i] == 0:
                chk[i] = 1
                # path.append(i)
                dfs(i)
                # path.pop(i)
                chk[i] = 0

N = int(input())
for _ in range(M):
    n, m = map(int, input().split())
    g = [[0]*(n+1) for _ in range(n+1)]
    chk = [0] * (n+1)
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
    cnt = 0
    # path = []
    # path.append(1)
    chk[1] = 1
    dfs(1)