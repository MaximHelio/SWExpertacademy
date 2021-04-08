def inorder(start):
    global ans
    if start * 2 <= N:
        inorder(start * 2)
    ans += tree[start]

    if start * 2 + 1 <= N:
        inorder(start * 2 + 1)


T = 10
for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    ans = ''
    for _ in range(N):
        temp = input().split()
        tree[int(temp[0])] = temp[1]

    inorder(1)
    print('#%d %s' % (tc, ans))