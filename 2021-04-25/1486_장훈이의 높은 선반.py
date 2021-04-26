def powerset(n, k):
    global ans
    if n == k:
        sum = 0
        for i in range(N):  # 부분집합의 원소의 합
            if bit[i]: sum += H[i]
        if sum >= B:    # 점원들의 키의 합이 선반보다는 커야함
            if ans > sum:
                ans = sum
    else:
        bit[k] = 1
        powerset(n, k+1)
        bit[k] = 0
        powerset(n, k+1)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())    # 점원 수, 선반의 높이
    H = list(map(int, input().split())) # 점원들의 키
    bit = [0] * N
    ans = 987654321
    powerset(N, 0)
    print('#%d %d' %(tc, ans-B))