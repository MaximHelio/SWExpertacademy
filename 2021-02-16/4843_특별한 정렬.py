import sys
sys.stdin = open("sample_input (2).txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    new_lst = []

    while len(lst) > 0:
        new_lst.append(max(lst))
        new_lst.append(min(lst))
        lst.remove(max(lst))
        lst.remove(min(lst))

    print("#%d" %tc, end=" ")
    for i in range(10):
        print(new_lst[i], end=" ")
    print()