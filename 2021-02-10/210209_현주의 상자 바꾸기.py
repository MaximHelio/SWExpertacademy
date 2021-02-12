import sys
sys.stdin = open("sample_input (5).txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split()) # 1 ≤ N, Q ≤ 103
    arr = [0] * N

    for idx in range(1, Q+1):
        Li, Ri = map(int, input().split())  # 1, 2, ...Q로 교체
        arr[Li-1:Ri] = [idx] * (Ri - Li + 1)

    print("#%d" %tc, end=" ")
    for i in arr:
        print(i, end=" ")
