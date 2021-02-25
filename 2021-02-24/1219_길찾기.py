import sys
sys.stdin = open("input (1).txt", "r")

def back(v):
    sw[v] += 1  # visited
    for i in arr[v]:
        if sw[i] >= 2: continue
        else: back(i)
    return

for tc in range(1, 11):
    T, E = map(int, input().split())
    arr = [[] for _ in range(100)]
    sw = [0]*100
    inp = list(map(int, input().split()))

    for i in range(E):
        arr[inp[2*i]].append(inp[2*i+1])

    back(0)
    print("#%d" % tc, end=" ")
    if sw[99]>0:
        print(1)
    else: print(0)
