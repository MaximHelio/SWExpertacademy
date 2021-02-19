import sys
sys.stdin = open("input (4).txt", "r")

def back(x, y, dir):
    global num
    arr[x][y] = num
    num += 1
    if num > N * N: return
    if dir == 'right':
        if y + 1 == N or arr[x][y + 1] != 0:
            back(x + 1, y, 'down')
            return
        back(x, y + 1, dir)
    if dir == 'left':
        if y - 1 == -1 or arr[x][y - 1] != 0:
            back(x - 1, y, 'up')
            return
        back(x, y - 1, dir)
    if dir == 'up':
        if x - 1 == -1 or arr[x - 1][y] != 0:
            back(x, y + 1, 'right')
            return
        back(x - 1, y, dir)
    if dir == 'down':
        if x + 1 == N or arr[x + 1][y] != 0:
            back(x, y - 1, 'left')
            return
        back(x + 1, y, dir)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    num = 1
    back(0, 0, 'right')
    print('#%d' % tc)
    for i in arr:
        print(*i)