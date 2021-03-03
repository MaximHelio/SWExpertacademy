import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M1, M2= map(int, input().split())
    arr = list(map(int, input().split()))
#####################################################
    com = min(M1, M2)
    diff = abs(M1-M2)

    M1_list = []
    M2_list = []
    for _ in range(com):
        M1_list.append(max(arr))
        arr.remove(max(arr))
        M2_list.append(max(arr))
        arr.remove(max(arr))
    for _ in range(diff):
        if M1 > M2:
            M1_list.append(max(arr))
            arr.remove(max(arr))
        else:
            M2_list.append(max(arr))
            arr.remove(max(arr))
    M1_sum = 0
    for i in range(len(M1_list)):
        M1_sum += M1_list[i] * (i+1)
    M2_sum = 0
    for j in range(len(M2_list)):
        M2_sum += M2_list[j] *(j+1)
    total = M1_sum + M2_sum
    print("#%d %d" %(tc, total))