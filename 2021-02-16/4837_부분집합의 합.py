import sys
sys.stdin = open("sample_input (3).txt", "r")

total_lst = [i for i in range(1, 13)]
# subset
lst = []
for i in range(1 << len(total_lst)):
    sub_lst = []
    for j in range(len(total_lst)):
        if i & (1 << j):
            sub_lst.append(total_lst[j])
    lst.append(sub_lst)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    result = 0

    for s in lst:
        if len(s) == N and sum(s) == K:
            result += 1
    print("#%d %d" %(tc, result))

