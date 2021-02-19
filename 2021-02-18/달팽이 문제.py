arr = [[9, 20, 2, 18, 11],
       [19, 1, 25, 3, 21],
       [8, 24, 10, 17, 7],
       [15, 4, 16, 5, 6],
       12, 13, 22, 23, 14]

# 0, 0 => 0, 1 => 0, 2 => 0, 3 => 0, 4 =>
#우측으로 가다가 경계를 만나면 아래로
# 아래의 경계를 좌측 => 위 =>
# 우 => 하 => 좌 => 상 => 우 => 하
dc = [1, 0, -1, 0]
dr = [0, 1, 0, -1]
dir = 0
dst = [[0 for _ in range(5)] for _ in range(5)]

if 경계를 만나거나 데이터가 들어있으면:
    dir = dir + 1
    if dir == 4:
        dir = 0

    dir = dir % 4

curR =
curC =
for i in range(N*N):
    dst[curR][curC] = getvalue()
    newR = curR + dr[dir]
    newC = curC + dc[dir]
    if newR < 0 or newR >=N or newC < 0 or newC >= N or dst[newR][newC] != 0:
        dir = dir % 4
        newR = curR + dr[dir]
        newC = curC + dc[dir]


# 풀이
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
    if dir == 'right': return x, y + 1
    if dir == 'left': return x, y - 1
    if dir == 'up': return x - 1, y
    if dir == 'down': return x + 1, y

def check(x, y):
    if x == N or x == -1 or y == N or y == -1 or arr[x][y] != 0: return False
    return True

def back(x, y, dir):
    global num
    arr[x][y] = num
    num += 1
    if num > N * N: return
    x2, y2 = pos(x, y, dir)
    if check(x2, y2) is False:
        back(x, y, dir_base[dir])
        return
    back(x2, y2, dir)

back(0, 0, 'right') # 2^N