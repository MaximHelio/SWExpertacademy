import sys
sys.stdin = open('sample_input (1).txt', 'r')

def f(root):
    if root:
        lv = f(root의 왼쪽)
        rv = f(root의 오른쪽)
        TREE[root] = lv + rv
        return lv + rv

T = int(input())
N, M, L = map(int, input().split())
for _ in range(M):
    tmp = map(int, input().split())
    tree = [[] for _ in range(N)]
