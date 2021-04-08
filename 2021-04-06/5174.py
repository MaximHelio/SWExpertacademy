#import sys
#sys.stdin = open('sample_input (6).txt', 'r')

def tr(root):
    global cnt
    if root:
        cnt += 1
        tr(tree[root][0])
        tr(tree[root][1])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())

    lst = list(map(int, input().split()))
    tree = [[0, 0] for _ in range(E+2)]
    for idx in range(0, len(lst), 2):
        p = lst[idx]
        c = lst[idx+1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c
    cnt = 0
    tr(N)
    print('#%d %d' %(tc, cnt))