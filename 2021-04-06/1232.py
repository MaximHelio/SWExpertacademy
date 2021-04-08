import sys
sys.stdin = open('input (1).txt', 'r')


T= 10
for tc in range(1, T+1):
    N = int(input()) # 5
    






# def dfs(n):
#     global cnt
#     # 배열크기 넘어가지 않도록
#     if n <= N:
#         # 좌측 노드
#         dfs(n * 2)
#         # 더이상 가지 못한다면
#         tree[n] = cnt
#         cnt += 1
#         # 우측 노드
#         dfs(n * 2 + 1)
#
#
# for tc in range(1, int(input())+1):
#     N = int(input())
#     # 1차원 배열
#     tree = [0 for i in range(N + 1)]
#     cnt = 1
#     dfs(1)
#     print('#%d %d %d' %(tc, tree[1], tree[N // 2]))
