T = int(input())
for tc in range(1, T+1):
    N = int(input())
    total_even = 0
    total_odd = 0
    for num in range(1, N+1):
        if num % 2 == 0:
            total_even += num
        elif num % 2:
            total_odd += num
    total = total_odd - total_even
    print("#%d %d" %(tc, total))