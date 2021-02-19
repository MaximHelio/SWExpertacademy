import sys
sys.stdin = open("input.txt", "r")

def snail(N, start, arr, idx):

    if N==1:
        arr[idx][idx] = start
        return arr
    #1
    # 첫 가로줄
    for i in range(N-1):
        arr[idx][idx+i] = start + i

    # 첫 세로줄
    for j in range(N-1):
        arr[idx+j][idx+N-1] = start + N-1 + j

    # 두번째 가로줄
    for k in range(N-1):
        arr[idx+N-1][idx+N-1 -k] = start+ 2 * (N-1) + k

    # 두번째 세로줄
    for l in range(N-1):
        arr[idx+N-1-l][idx] = start + 3 * (N-1) + l

    if N==2:
        return arr

    snail(N-2,start+4*N-4,arr,idx+1)

    return arr


T = int(input())
for tc in range(1, T+1):
   N = int(input())
   arr = [[0] * N for _ in range(N)]
   l_snail = snail(N,1,arr,0)

   print('#%d' % tc)

   for i in range(N):
       print(*l_snail[i])


