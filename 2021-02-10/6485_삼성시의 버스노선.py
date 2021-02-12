import sys
sys.stdin = open("input (5).txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Ai = list(map(int, input()))
    Bi = list(map(int, input()))
    P = int(input())
    arr = []
    for i in range(len(P)):
        cnt = 0
        for j in range(N):
            if A[j] <= P[i] <= B[j]:
                cnt +=1
            arr.append(cnt)
print("#%d %d" .format(tc, *arr))