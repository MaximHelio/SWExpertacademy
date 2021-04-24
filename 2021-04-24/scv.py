n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = arr[0][0]
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0: continue
        M = -1
        if i-1 >= 0 and M < dp[i-1][j]: M = dp[i-1][j] # 위쪽에서 옴
        if j-1 >= 0 and M <= dp[i][j-1]: M = dp[i][j-1] # 왼쪽에서 옴
        dp[i][j] = arr[i][j] + M
print(dp[n-1][n-1])