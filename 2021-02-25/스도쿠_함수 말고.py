import sys
sys.stdin = open("input (2).txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    cnt = 0 # 검사를 통과한 횟수
    # 가로줄 검사
    for i in range(9):
        row = []
        for j in range(9):
            row.append(arr[i][j])
        if len(set(row)) != 9: result = 0
        else:
            for item in set(row):
                if item not in num: result = 0
                else: cnt += 1
    # 세로줄 검사
    for j in range(9):
        col = []
        for i in range(9):
            col.append(arr[i][j])
        if len(set(col)) != 9: result = 0
        else:
            for item in set(col):
                if item not in num: result = 0
                else: cnt += 1

    # 3*3 격자 검사
    row = [1, 4, 7]
    col = [1, 4, 7]

    for i in row:
        for j in col:
            grid = []
            grid.extend([arr[i][j], arr[i-1][j-1], arr[i-1][j], arr[i-1][j+1], arr[i+1][j], arr[i][j-1], arr[i][j+1], arr[i+1][j], arr[i+1][j-1], arr[i+1][j+1]])
            if len(set(grid)) != 9: result = 0
            else:
                for item in set(grid):
                    if item not in num: result = 0
                    else: cnt += 1
    print(cnt)
    if cnt == 243: result = 1
    print("#%d %d" %(tc, result))