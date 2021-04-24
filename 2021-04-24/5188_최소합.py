import sys
sys.stdin = open('sample_input (17).txt')

def bfs(x, y):
    global total
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx > N-1: continue
        if nx < 0 or nx > N-1: continue
        total += arr[nx][ny]

T = int(input())
#      상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    bfs(0, 0)
    total = 0
    print('#%d %d' %(tc, total))
