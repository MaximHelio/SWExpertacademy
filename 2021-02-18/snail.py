N = 11

arr = [[0] * N for _ in range(N)]
num = 1

#*어떤 경우든 브레이크 포인트면 멈춤
#F7 : 한줄 실행하기 (만약, 함수면 함수 안으로 들어가기)
#F8 : 한줄 실행하기
#F9 : 그냥 무시하고 쭉 진행하기 (브레이크포인트면 멈춤)
dir_base = {
    'right': 'down',
    'left': 'up',
    'up': 'right',
    'down': 'left'
}

def pos(x, y, dir):
    if dir == 'right': return x, y + 1, dir_base[dir]
    if dir == 'left': return x + 1,  y, dir_base[dir]
    if dir == 'up': return x + 1, y, dir_base[dir]
    if dir == 'down': return x + 1, y, dir_base[dir]

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

back(0, 0, 'right')
print(arr)
for i in arr:
    print(i)