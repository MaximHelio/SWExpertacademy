import sys
sys.stdin = open("input (7).txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    prime = [2, 3, 5, 7, 11]
    cnt = [0] * 5

    for i in range(len(prime)):
        while N % prime[i] == 0:
            cnt[i] += 1
            N //= prime[i]

    print("#{} {}" .format(tc, " ".join(map(str, cnt))))