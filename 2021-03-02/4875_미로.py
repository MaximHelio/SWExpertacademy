import sys
sys.stdin = open("sample_input (1).txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 2:
                start = arr[i][j]
    for