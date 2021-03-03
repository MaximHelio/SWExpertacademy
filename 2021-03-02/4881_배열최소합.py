import sys
sys.stdin = open("sample_input (2).txt", "r")

def per(k, midV):
    global minV
    if minV < midV:
        return

    if k==N:
        sumV = 0
        for k in range(N):
            idx = sel[k]
            sumV += BRD[k][idx]
        if minV < sumV:
            minV = sumV

    for i in range(N):
        if not visited[i]:
            sel[k] = i
            visited[i] = True
            idx = sel[k]
            sumV += BRD[k][i]
            per(k+1, midV + BRD[k][i])
            visited[i] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    minV = 1e10
    arr = [list(map(int, input().split())) for _ in range(N)]
    per(0)
    print("#{} {}".format(tc, minV))
