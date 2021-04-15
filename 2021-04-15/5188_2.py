import sys
sys.stdin = open('sample_input (8).txt')

def dfs(row, col):
    down = right = N * 11
    if row == col >= N-1:
        return arr[row][col]
    else:
        if row < N-1:
            down = dfs(row+1, col)
        if col < N-1:
            right = dfs(row, col+1)
    if down < right:
        return arr[row][col] + down
    return arr[row][col] + right

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print('#%d %d' %(tc, dfs(0, 0)))