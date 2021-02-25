def snail(x, y, dir):
    global num
    arr[x][y] = num
    if num == K:
        print(y + 1, end=" ")
        print(R - x)
        return
    num += 1
    if dir == 'up':
        if x - 1 == -1 or arr[x-1][y] != 0:
            snail(x, y+1, 'right')
            return
        snail(x - 1, y, dir)
    if dir == 'right':
        if y + 1 == C or arr[x][y+1] != 0:
            snail(x+1, y, 'down')
            return
        snail(x, y + 1, dir)
    if dir == 'down':
        if x + 1 == R or arr[x+1][y] != 0:
            snail(x, y-1, 'left')
            return
        snail(x + 1, y, dir)
    if dir == 'left':
        if y-1 == -1 or arr[x][y-1] != 0:
            snail(x-1, y, 'up')
            return
        snail(x, y - 1, dir)

C, R = map(int,input().split())
K = int(input())
arr = [[0] * C for _ in range(R)]
num = 1
snail(R-1, 0, 'up')

