import sys
sys.stdin = open('input (27).txt')

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    rem = sum(height) - B

    def subset(k, i, j):
        global ans
        if i >= B:  # 0 >= 16
            ans = min(ans, i - B)   # min(98765421, 1)
            return
        if j > rem:   # 0 > 2 포함 안한 게 이미 전체에서 장훈이 키를 뺀 것보다 크다면 더 해도 만들 수 없음
            return
        if k == N:  # 0 == 5 다 돌았다면
            return
        subset(k + 1, i + height[k], j)  # subset(1, 1, 0) 포함했을 때
        subset(k + 1, i, j + height[k])  # subset(1, 0, 1) 안했을 때

    ans = 987654321
    subset(0, 0, 0)
    print('#%d %d' %(tc, ans))