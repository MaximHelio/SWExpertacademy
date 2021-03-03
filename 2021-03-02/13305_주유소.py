N = int(input()) # 도시의 수
d = list(map(int, input().split())) # 거리의 수
price = list(map(int, input().split())) # 유류비

total = 0
for i in range(len(price)):
    for j in range(len(d)):
        while price[i] < price[i+1]:
            price[i] * d[i+]
