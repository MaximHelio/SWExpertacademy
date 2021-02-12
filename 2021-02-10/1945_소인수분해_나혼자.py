import sys
sys.stdin = open("input (7).txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prime = [2, 3, 5, 7, 11]
    cnt = [0] * 5

    for idx in range(len(prime)):
        while N % prime[idx] == 0:
            cnt[idx] +=1
            N //= prime[idx]

    print("#{} {}" .format(tc, " ".join(map(str, cnt))))