N = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

total = dist[0] * price[0]
min_price = price[0]
meter = 0
for i in range(1, N-1):
    if price[i] < min_price:
        total += min_price * meter
        meter = dist[i]
        min_price = price[i]
    else:
        meter += dist[i]
    if i == N-2:
        total += min_price * meter
print(total)