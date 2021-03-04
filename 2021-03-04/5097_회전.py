import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Q = list(map(int, input().split()))
    for _ in range(M):
        Q.append(Q.pop(0))
    print("#%d %d" %(tc, Q[0]))