import sys
sys.stdin = open("input.txt", "r")

def maze(row, col):
    global ans
    if arr[row][col] == 3 or ans:
        ans = 1
        return
    for dr, dc in dir:
        newR = row + dr
        newC = col + dc
        if arr[newR][newC] != 1:
            arr[row][col] = 1 # 현재 위치
            maze(newR, newC)

T = 10
for _ in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ans = 0
    maze(1, 1)
    print("#%d %d" %(tc, ans))