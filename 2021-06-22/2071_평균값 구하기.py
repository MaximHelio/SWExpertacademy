T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    num = len(arr)
    avg = round(sum(arr) / num)
    print("#%d %d" %(tc, avg))