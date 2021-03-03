T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    t = D / (A+B)
    distance = t * F
    print("#%d %.8f" %(tc, distance))