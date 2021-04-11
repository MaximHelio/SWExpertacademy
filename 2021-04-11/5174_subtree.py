def inorder(node):
    global cnt
    if node == 0:
        return
    cnt += 1
    inorder(left[node])
    inorder(right[node])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    tree = list(map(int, input().split()))
    left = [0] * (E+2)
    right = [0] * (E+2)
    for i in range(0, len(arr), 2):
        parent, baby = arr[i], arr[i+1]
        if left[parent]:
            right[parent] = baby
        else:
            left[parent] = baby
    cnt = 0
    inorder(N)
    print('#%d %d' %(tc, cnt))