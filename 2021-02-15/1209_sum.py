import sys
sys.stdin = open("input (6).txt", "r")

T = 10
for tc in range(1, T+1):
    N =int(input())
    arr = []
    for i in range(100):
        arr. append(list(map(int, input().split())))
    result = []

    # 각 행의 합
    for y in range(len(arr)):
        sum_row = 0
        for x in range(len(arr)):
            sum_row += arr[y][x]
        result.append(sum_row)

    # 각 열의 합
    for x in range(len(arr)):
        sum_col = 0
        for y in range(len(arr)):
            sum_col += arr[y][x]
        result.append(sum_col)

    # 각 대각선의 합
    sum_diagonal_left= 0
    for y in range(len(arr)):
        sum_diagonal_left += arr[y][y]
    result.append(sum_diagonal_left)

    sum_diagonal_right = 0
    for y in range(len(arr)):
        for x in range(len(arr)):
            if y == len(arr)-x:
                sum_diagonal_right += arr[y][x]
    result.append(sum_diagonal_right)

    print("#%d %d" %(tc, max(result)))