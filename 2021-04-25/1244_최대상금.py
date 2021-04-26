import sys
sys.stdin = open('input (33).txt')

d = [1, 10, 100, 1000, 10000, 100000]
visit = [[0] * 1000000 for _ in range(11)]
for tc in range(1, int(input()) + 1):
    arr, N = map(str, input().split())
    L = len(arr)
    N = int(N)

    ans = 0


    def backtrack(k, val):
        if visit[k][val] == tc: return
        visit[k][val] = tc

        if k == N:
            global ans;
            ans = max(ans, val)
        else:
            for i in range(L - 1):
                for j in range(i + 1, L):
                    a = (val // d[i]) % 10
                    b = (val // d[j]) % 10
                    t = val - a * d[i] + b * d[i] - b * d[j] + a * d[j]
                    backtrack(k + 1, t)


    backtrack(0, int(arr))
    print('#{} {}'.format(tc, ans))