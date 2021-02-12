import sys
sys.stdin = open('input (4).txt', 'r')


# def find(V, K, N, M):
#     V.insert(0,0)
#     V.append(N)
#     for i in range(1, M+2):
#         if V[i]-V[i-1] > K:
#             return 0
#
#         if V[i] > last + K:
#             last = V[i-1]
#             cnt += 1
#
#     return cnt


T = int(input())
for tc in range(1, T+1):
    # K: 이동할 수 있는 거리
    # N: 마지막 종점의 위치
    # M: 충전소의 개수
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    bus_stop = [0] * (N+1)
    ans = 0

    for i in charge:
        bus_stop[i] = 1
    bus = 0 # 버스 위치
    ans = 0 # 충전 횟수

    while True:
        # 버스가 이동할 수 있는 만큼 이동을 하자
        bus += K
        if bus >= N: break #  종점에 도착하거나 종점을 지나 더 나아간 경우

        for i in range(bus, bus - K, -1):
            # if bus_stop[i] == 1:
            if bus_stop[i]:
                ans += 1
                bus = i
                break
            # 충전기를 못 찾았을 때
            else:
                ans = 0
                break

    print("#{} {}" .format(tc, ans))