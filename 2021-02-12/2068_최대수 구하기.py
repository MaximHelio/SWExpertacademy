T = int(input())
for tc in range(1, T+1):
    inp = list(map(int, input().split()))
    max_num = inp[0]
    for num in inp:
        if num >= max_num:
            max_num = num
    print("#%d %d" %(tc, max_num))