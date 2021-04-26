'''
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10} 부분집합의 합이 10이 되는 경우를 출력하시오
'''
def powerset(n, k, cursum):
    global cnt
    cnt += 1

    if cursum > 10: # 가지치기
        return
    if n == k:
        if cursum == 10:    # 합이 10이 되는 경우만 출력
            for i in range(N):
                if bit[i]:
                    print(arr[i], end=" ")
            print()
    bit[k] = 1  # 체크
    powerset(n, k+1, cursum+arr[k])
    bit[k] = 0  # 체크 x
    powerset(n, k+1, cursum)


arr = range(1, 10+1)
N = len(arr)
bit = [0] * N
cnt = 1
powerset(N, 0, 0)
print(cnt)
