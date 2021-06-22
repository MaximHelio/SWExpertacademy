T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    result = max(arr)
    print("#%d %d" %(tc, result))