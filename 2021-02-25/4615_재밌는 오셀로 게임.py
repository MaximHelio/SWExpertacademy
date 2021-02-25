import sys
sys.stdin = open("sample_input(1).txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    osello = [[0] * N for _ in range(N)]
    inp = [list(map(int, input().split())) for _ in range(M)]

    cnt1 = 0
    for i in range(M):
        for j in range(3):
            # 시도했던 흑돌의 개수
            if inp[i][2] == 1:
                cnt1 += 1
            # 시도했던 백돌의 개수
            else: cnt2 += 1

    for i in range(N):
        for j in range(N):
            if inp[i][0] == inp[i][1]:
