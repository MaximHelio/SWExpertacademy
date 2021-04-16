import sys
sys.stdin = open('sample_input (2).txt')

T = int(input())
for tc in range(1, T+1):
#  컨테이너의 수, 트럭의 수
    N, M = map(int, input().split())
    wi_list = list(map(int, input().split()))
    ti_list = list(map(int, input().split()))
    wi_sum = sum(wi_list)
    print(wi_list)

    wi_list.sort(reverse=True)
    if len(wi_list) <= len(ti_list):
        for wi in wi_list:
            wi_truck_list = []
            for ti in ti_list:
                if wi <= ti: wi_truck_list.append(ti)
            if len(wi_truck_list) == 0:
                total = wi_sum - wi
            else: total = wi_sum
    else:

    ####교수님 풀이

Nlst = []
Mlst = []
Nlst.sort(reverse=True)
Mlst.sort(reverse=True)

for w in Mlst:
    while idx < N and Nlst[idx] < w:
        idx += 1

    total += Nlst[idx]
    idx += 1
    if idx == N-1:
        idx += 1
    else:
        break