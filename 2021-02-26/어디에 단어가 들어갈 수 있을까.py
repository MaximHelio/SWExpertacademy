import sys
sys.stdin = open("input (1).txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        check_r = 0
        check_c = 0
        for j in range(N):
            # 가로 확인 K = 3
            if arr[i][j] == 1:
                check_r += 1
            else: # arr[i][j] == 0
                if check_r == K: cnt += 1
                check_r = 0
            # 세로 확인
            if arr[j][i] == 1: check_c += 1
            else: #arr[j][i] == 0
                if check_c == K: cnt += 1
                check_c = 0
        if check_r == K: cnt += 1
        if check_c == K: cnt += 1

    print("#%d %d" %(tc, cnt))






























































    +
