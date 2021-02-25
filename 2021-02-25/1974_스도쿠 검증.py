import sys
sys.stdin = open("input (2).txt", "r")

def sudoku(arr):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    cnt = 0 # 검사를 통과한 횟수

    # 가로줄 검사
    for i in range(9):
        row = set()
        for j in range(9):
            row.add(arr[i][j])
        if len(row) != 9: return 0
        else:
            for item in row:
                if item not in num: return 0
    cnt += 1

    # 세로줄 검사
    for j in range(9):
        col = set()
        for i in range(9):
            col.add(arr[i][j])
        if len(set(col)) != 9: return 0
        else:
            for item in set(col):
                if item not in num: return 0
    cnt += 1

    # 3*3 격자 검사
    row = [1, 4, 7]
    col = [1, 4, 7]
    grid = []
    for i in row:
        for j in col:
            grid.extend([arr[i][j], arr[i-1][j-1], arr[i-1][j], arr[i+1][j], arr[i][j-1], arr[i+1][j], arr[i+1][j-1], arr[i+1][j], arr[i+1][j+1]])
            if len(set(grid)) != 9: return 0
            else:
                for item in set(grid):
                    if item not in num: return 0
        cnt += 1

    if cnt == 3: return 1

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print("#%d %d" %(tc, sudoku(arr)))