import sys
sys.stdin = open("input (18).txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    #상하 대칭 이용
    sum = 0
    for i in range(N//2+1):
        for k in range(-i, i+1, 1):
            sum += arr[i][N//2 + k]
    for i in range(N-1, N//2, -1):
        for k in range(-N+1+i, N-i, 1):
            sum += arr[i][N//2 + k]
    print("#%d %d" %(tc, sum))


