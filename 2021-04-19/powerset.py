def powerset(n, k):
    if n == k:
        # print(bit)
        # for i in range(N):
        #     if bit[i]: print(arr[i], end=" ")
        # print()
        sum = 0
        for i in range(N): # 원소의 합
            if bit[i]:
                sum += arr[i]
                
        if sum == 10: # 합이 10이 되는 경우만 출력
            for i in range(N):
                if bit[i]: print(arr[i], end=" ")
            print()
    else:
        bit[k] = 1
        powerset(n, k+1)
        bit[k] = 0
        powerset(n, k+1)

arr = [1, 2, 3]
N = len(arr)
bit = [0] * N
powerset(N, 0)