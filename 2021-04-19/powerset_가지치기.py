def powerset(n, k, cursum):
    global cnt
    cnt += 1

    if cursum > 10: return # 가지치기

    if n == k:
        if sum == 10:  # 합이 10이 되는 경우만 출력
            for i in range(N):
                if bit[i]: print(arr[i], end=" ")
            print()
    else:
        bit[k] = 1
        powerset(n, k + 1, cursum + arr[k])
        bit[k] = 0
        powerset(n, k + 1, cursum)


arr = [1, 2, 3]
N = len(arr)
bit = [0] * N
cnt = 1 # 이 위치에 넣어야 powerset이 cnt를 바꿈
powerset(N, 0, 0)
print(cnt)