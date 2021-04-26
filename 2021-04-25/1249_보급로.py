import sys
sys.stdin = open('input (30).txt')

diff = [(1, 0), (-1, 0), (0, 1), (0, -1)]
T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 4

    arr = [list(map(int, input())) for _ in range(N)]
    # 무한대로 초기화 0xffff로도 할 수 있음
    D = [[99999999999999999] * N for _ in range(N)]
    D[0][0] = arr[0][0]

    while True:
        flag = True
        for x in range(N):
            for y in range(N):
                for dx, dy in diff:
                    nx, ny = x+dx, y+dy
                    if nx < 0 or nx > N-1 or ny < 0 or ny > N-1 : continue
                    if D[nx][ny] > D[x][y] + arr[nx][ny]:
                        D[nx][ny] = D[x][y] + arr[nx][ny]
                        flag = False
        if flag: break

    print('#%d %d' %(tc, D[N-1][N-1]))


