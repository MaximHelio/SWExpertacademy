def imugi(arr, row, column):
    """
   주어진 2차원 배열의 시작점(row, column)에서 출발하여, 올라가다가 좌우 사다리를 만나면 꺾어서 그 다음 세로 사다리 지점까지
   도달하는 '승천하는 이무기 함수' 이다. 이무기 함수는 올라갈 때 좌우의 값이 1이 아닌지 체크하며 올라가며,
   만약 어느새 꼭대기까지 올라갔다면, 그 때 있던 column을 반환하게 된다. 작동은 재귀적으로 이루어진다.
    """
    col_end = 0
    row_end = 0
    # 재귀적으로 다음 이무기에게 먹여줄 row, column을 미리 초기화

    for i in range(row, -1, -1):  # 시작점부터 세로로 올라가며 좌우의 1을 검사/ 혹은 이미 꼭대기인지 검사

        if range[i][column - 1] == 1:
            for j in range(column - 1, -1, -1):  # 가로로 왼쪽 끝까지 검사
                if range[i][j] == 0:  # 왼쪽으로 가다가 0을 만나면 그 직전 위치(j+1)가 새로운 시작점
                    row_end = i
                    col_end = j + 1

        elif range[i][column + 1] == 1:
            for j in range(column + 1, 100, 1):  # 가로로 오른쪽 끝까지 검사
                if range[i][j] == 0:  # 오른쪽으로 가다가 0을 만나면 그 직전 위치(j-1)가 새로운 시작점
                    row_end = i
                    col_end = j - 1
        elif i == 0:
            return column

    return imugi(arr, row_end, col_end)


for test_case in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    start = 0
    for i in range(100):
        if arr[99][i] == 2:
            start = i

    print("#%d %d" %(N, imugi(arr, 99, start)))