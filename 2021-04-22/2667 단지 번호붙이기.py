# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# def dfs(x, y):
#     global cnt  # 0
#     cnt += 1
#     board[x][y] = 0 # 다시 방문하지 못하도록
#     for i in range(4):
#         X = x+dx[i]
#         Y = y+dy[i]
#         # 경계조건
#         if 0 <= X < n and 0 <= Y < n and board[X][Y] ==1:
#             dfs(X, Y)
#
# n = int(input())
# board = [list(map(int,input())) for _ in range(n)]
# result = []
# for i in range(n):
#     for j in range(n):
#         if board[i][j] == 1:
#             cnt = 0
#             dfs(i, j)
#             result.append(cnt)
# print(len(result))
# result.sort()
# for x in result:
#     print(x)


def dfs(x, y):
    global cnt
    cnt += 1
    board[x][y] = 0
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if 0 <= X < N and 0 <= Y < N and board[X][Y] == 1:
            dfs(X, Y)
#     상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = int(input())
board = [list(map(int, input())) for _ in range(N)]
result = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            cnt = 0
            dfs(i, j)
            result.append(cnt)
print(len(result))
result.sort()
for x in result:
    print(x)
