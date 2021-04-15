import sys
sys.stdin = open('sample_input (8).txt')

def issafe(x, y):
    return 0 <= y < N and 0 <= x < N

def dfs(x, y):
    global sub_result, result
    if result < sub_result:
        return
    if y == N-1 and x == N-1:
        result = sub_result
        return
    for dir in range(2):
        X = x + dx[dir]
        Y = y + dy[dir]
        if issafe(X, Y) and (X, Y) not in visited:
            visited.append((X, Y))
            sub_result += arr[X][Y]
            dfs(X, Y)
            visited.remove((X, Y))
            sub_result -= arr[X][Y]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    dx = [1, 0]
    dy = [0, 1]

    sub_result, result = arr[0][0], 987654321
    dfs(0, 0)
    print('#%d %d' %(tc, result))