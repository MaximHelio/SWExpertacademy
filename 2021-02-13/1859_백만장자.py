import sys
sys.stdin = open("input (13).txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    max_price = price[0]
    for item in price:
        if item >= max_price:
            max_price = item
    print(max_price)


