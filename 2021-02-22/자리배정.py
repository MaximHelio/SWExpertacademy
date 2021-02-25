def seat(x, y, dir):
    global num
    print(x, y)
    arr[x][y] = num
    num += 1
    if num > R * C:  return 0
    if dir == 'up':
        print('up')
        if y + 1 == C or arr[x-1][y] != 0:
            seat(x, y+1, 'right')
            return
        seat(x, y+1, dir)
    if dir == 'right':
        if y + 1 == C or arr[x][y+1] != 0:
            seat(x+1, y, 'down')
            return
        seat(x+1, y, dir)
    if dir == 'down':
        if x + 1 == R or arr[x+1][y] != 0:
            seat(x, y-1, 'left')
            return
        seat(x, y-1, dir)
    if dir == 'left':
        if y-1 == -1 or arr[x][y-1] != 0:
            seat(x-1, y, 'up')
            return
        seat(x-1, y, dir)

C, R  = map(int, input().split())
arr = [[0]* C for _ in range(R)] # : arr[0~5][0~6]
num = 1
num_inp = int(input())
seat(R-1, 0, 'up')
print(arr)

