import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum_list = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for k in range(M):
                for l in range(M):
                    sum += arr[i+k][j+l]
            sum_list.append(sum)
    print("#%d %d" %(tc, max(sum_list)))