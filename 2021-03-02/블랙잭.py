from itertools import combinations

N, M = map(int, input().split())
arr = list(map(int, input().split()))
a = list(combinations(arr, 3))
comb = []
for item in a:
    if sum(item) <= M:
        comb.append(sum(item))

min_num = comb[0]
for num in comb:
    if abs(M - num) < abs(M - min_num):
        min_num = num
print(min_num)

