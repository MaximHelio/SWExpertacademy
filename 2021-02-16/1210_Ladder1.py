import sys
sys.stdin = open("input.txt", "r")


def imugi(arr, row, column):
    col_end = 0
    row_end = 0
    #row, column을 미리 초기화

    for i in range(row, -1, -1):  # 시작점부터 세로로 올라가며 좌우의 1을 검사/ 혹은 이미 꼭대기인지 검사

        if column >= 1 and arr[i][column - 1] == 1:  # 왼쪽에 사다리를 만난다면
            for j in range(column - 1, -1, -1):  # 가로로 왼쪽 끝까지 검사
                if arr[i - 1][j] == 1:
                    return imugi(arr, i - 1, j)
                    # row_end = i-1
                    # col_end = j
                    # break
            # break

        elif column <= 98 and arr[i][column + 1] == 1:  # 오른쪽에 사다리를 만난다면
            for j in range(column + 1, 100, 1):  # 가로로 오른쪽 끝까지 검사
                if arr[i - 1][j] == 1:
                    return imugi(arr, i - 1, j)
                    # row_end = i-1
                    # col_end = j
                    # break
            # break

        elif i == 0:
            return column


for test_case in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    start = 0
    for i in range(100):
        if arr[99][i] == 2:
            start = i

    print("#%d %d" % (N, imugi(arr, 99, start)))

# T = 10
# for tc in range(1, T+1):
#      t = int(input())
#      N = 100
#      arr = [list(map(int, input().split())) for _ in range(N)]
#      print(arr)
#      for i in range(100):
#          for j in range(100):
#              if arr[i][j] == 2:     # 시작점 찾기
#                  start = arr[i][j]
#                  start_x = i
#                  start_y = j
#              if arr[i][j] == 1:



