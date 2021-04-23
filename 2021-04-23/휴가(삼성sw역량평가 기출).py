def dfs(L, sum):
    global res
    if L == n+1:
        if sum > res:
            res = sum
    else:
        if L+T[L] <= n+1:
            dfs(L+T[L], sum+P[L])
        dfs(L+1, sum)


n = int(input())
T = list()
P = list()
for _ in range(n):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)
res = -21470000
T.insert(0, 0)
P.insert(0, 0)
dfs(1, 0)
print(res)