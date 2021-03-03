import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    print(arr)
    # 가로줄 검사
    for i in range(N):
        cnt = 0
        for j in range(N-5+1):
            for k in range(5):
                if arr[i][j+k] == 'o': cnt += 1
            if cnt >= 5: ans = "YES"
        # 세로줄 검사
        cnt = 0
        for j in range(N-5+1):
            for k in range(5):
                if arr[j+k][i] == 'o': cnt += 1
            if cnt >= 5: ans = "YES"
        # 대각선 검사 좌상 => 우하
        cnt = 0
        arr[i][i] == 'o': cnt += 1
        if cnt >= 5: ans = "YES"
        # 대각선 검사 우상 => 좌하
        cnt = 0
        arr[i][N-i] == 'o': cnt += 1
        if cnt >= 5: ans = "YES"
    ans = "NO"
