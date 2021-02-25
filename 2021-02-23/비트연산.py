arr = [1, 4, 5]

for i in range(2):
    for j in range(2):
        for k in range(2):
            if i == 1: print(arr[0], end=' ')
            if j == 1: print(arr[1], end=' ')
            if k == 1: print(arr[2], end=' ')
            print()
n = 3
for i in range(2^n): # 2^n == 1 << n
    for j in range(n):
        p = i & (1<<n)
        if p != 0:
            print(1)
        if i & (1<<n):
            print(arr[j])

        p가 j번째 위치
        j = 0: x x p & 0 0 1
        j = 1: x p x & 0 1 0
        j = 2: p x x & 1 0 0

# p 위치의 bit 확인하는 법:
#     x x p x x: 0 0 p 0 0 => 0 0 0 0 0
#     x x p x x            => 0 0 1 0 0
#   & 0 0 1 0 0
#                0 0 p 0 1
#                0 0 1 0 0
#                        0
        if p != 0:
            print(1)
        else: print(0)

0 0 0: 0
0 0 1: 1
0 1 0: 2
0 1 1
1 0 0
1 0 1
1 1 0: 6
1 1 1: 7 (8-1: 2^3 -1)
1000