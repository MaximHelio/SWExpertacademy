import sys
from collections import deque

# 섬나라 아일랜드의 지도가 격자판의 정보로 주어진다.
# 각 섬은 1로 표시되어 상하좌우와 대각선으로 연결되어 있으며
# 0은 바다이다. 섬나라 아일랜드에 몇 개의 섬이 있는지 구하는 프로그램을 작성하세요.
# 입력 설명
#   서, 북서, 북, 북동, 동, 남동, 남, 남서

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
Q = deque()
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            board[i][j] = 0
            Q.append((i, j))
            while Q:
                tmp = Q.popleft()
                for k in range(8):
                    x = tmp[0]+dx[k]
                    y = tmp[1]+dy[k]
                    if 0 <= x < n and 0 <= y < n and board[x][y] == 1:
                        board[x][y] = 0
                        Q.append((x, y))
            cnt += 1 # 섬의 개수
print(cnt)