# import sys
# sys.stdin = open("1번_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N): # 가장 왼쪽 세로줄 부터 한 줄씩 띄어서 가장 최대로 나무가 심어지도
        for j in range(M):
            if j % 2:
                arr[i][j] = 0
    # 나무 심는 총 비용 계산
    sum = 0
    for i in range(N):
      for j in range(M):
          sum += arr[i][j]
    ans1 = sum
    # 심은 나무의 수 계산
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                cnt += 1
    ans2 = cnt

    # 가장 비싼 나무의 가격
    max_price = arr[0][0]
    for i in range(N):
        for j in range(M):
            if arr[i][j] > max_price:
                max_price = arr[i][j]
    ans3 = max_price

    # 가장 비싼 나무가 심어진 열(max가격이 중복될 경우, 인덱스 크기가 더 큰 것 출력)
    col_list = [] # 가장 비싼 나무가 심어진 열들
    for i in range(N):
        for j in range(M):
            if arr[i][j] == max_price:
                col_list.append(j)
    max_col_num = 0
    for col_num in col_list:
        if col_num > max_col_num:
            max_col_num = col_num
    ans4 = max_col_num + 1 # 인덱스를 0부터 셌으므로 문제에 맞게 바꿔줌

    print("#%d %d %d %d %d" %(tc, ans1, ans2, ans3, ans4))