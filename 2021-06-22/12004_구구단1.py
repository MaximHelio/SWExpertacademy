import sys
sys.stdin = open("sample_input (7).txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for i in range(1, 10):
        for j in range(1, 10):
            arr.append(i*j)
    if N in arr: result = "Yes"
    else: result = "No"
    print("#%d %s" %(tc, result))
