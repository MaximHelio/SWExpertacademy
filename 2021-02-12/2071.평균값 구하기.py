
T = int(input())
for tc in range(1, T+1):
    N = list(map(int, input().split()))
    cnt = len(N)
    sum = 0
    result = 0
    for num in N:
        sum += num
    result = sum / cnt
   print("#%d %d" %(tc, round(result)))