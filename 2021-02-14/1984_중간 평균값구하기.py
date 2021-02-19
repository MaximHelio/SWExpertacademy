T = int(input())
for tc in range(1, T+1):
    N = list(map(int, input().split()))

    max_num = N[0]
    min_num = N[0]
    total = 0
    cnt = len(N)
    for num in N:
        total += num
        if num >= max_num:
            max_num = num
        if num <= min_num:
            min_num = num
    average = round((total-max_num-min_num)/ (cnt-2))
    print("#%d %d" %(tc, average))
