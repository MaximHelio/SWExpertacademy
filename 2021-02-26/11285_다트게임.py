import sys
sys.stdin = open("s_input (1).txt", "r")

T = 1
for tc in range(1, T+1):
    N = int(input())
    x, y = map(int, input().split())
    sum = 0
def score(x, y):
    if x**2 + y**2 > 200**2:
        sum += 0
    else:
        for p in range(1, 11):
            if (20 * (11-(p+1)))**2 < x**2 + y**2 <= (20*(11-p))**2:
                sum += p

    print("#%d %d" %(tc, sum))
