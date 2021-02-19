import sys
sys.stdin = open("input (1).txt", "r")


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N은 5이상 15이하, M은 2이상 N 이하
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum_lst = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for k in range(M):
                for l in range(M):
                    sum += arr[i+k][j+l]
            sum_lst.append(sum)
    print("#%d %d" %(tc, max(sum_lst)))