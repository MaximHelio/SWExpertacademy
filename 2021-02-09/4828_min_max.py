import sys
sys.stdin = open("sample_input.txt", "r")

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Ai = list(map(int, input().split()))
    max_num = Ai[0]
    min_num = Ai[0]
    ans = 0
    for i in range(1, len(Ai)):
        if Ai[i] >= max_num: max_num = Ai[i]
        if Ai[i] < min_num: min_num = Ai[i]
        ans = max_num - min_num

    print("#%d %d" %(tc, ans))