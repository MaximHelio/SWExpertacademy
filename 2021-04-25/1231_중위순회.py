import sys
sys.stdin = open('input (32).txt')

def inorder(start):
    global ans
    if start * 2 <= N:
        inorder(start*2)
    ans += tree[start]
    if start * 2 + 1 <= N:
        inorder(start*2+1)


T = 10
for tc in range(1, T+1):
    N = int(input()) # 8
    tree = [0] * (N + 1)
    for _ in range(N):
        arr = input().split()
        tree[int(arr[0])] = arr[1]
    ans = ""
    inorder(1)
    print('#%d %s' %(tc, ans))