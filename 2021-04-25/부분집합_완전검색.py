def powerset(n, k):
    global cnt
    cnt += 1
    if n == k:
        sum =0
        for i in range(N): # 원소의 합
            if bit[i]:
                sum += arr[i]
        if sum == 10:   # 합이 10이 되는 경우만 출력
            for i in range(N):
                if bit[i]: print(arr[i], end=" ")
            print()
    else:
        bit[k] = 1
        powerset(n, k+1)
        bit[k] = 0
        powerset(n, k+1)


arr = range(1, 10+1)
N = len(arr)
bit = [0] * N
cnt = 1
powerset(N, 0)
print(cnt)