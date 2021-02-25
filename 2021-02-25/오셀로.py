############ 위아래왼오른쪽, 대각선 왼위, 왼아래, 오른위, 오른아래로 오셀로판 체크 후 칩을 뒤집는 8개의 함수.

def left(x, y, color):  # 착수점으로부터 왼쪽으로 채운다
    if y == 0: return  # 왼쪽 경계에 놓았으면 끝낸다.
    temp = 0
    for i in range(y - 1, -1, -1):  # 왼쪽 끝까지
        if osello[x][i] == color:
            break  # 같은 색을 만나면 for문을 빠져나온다.
        elif i == 0 or osello[x][i] == 0:
            return  # 같은 색이 아닌데, 경계점이거나, 같은 색을 만나기 전에 빈 칸을 만나면 함수를 끝낸다.
        elif osello[x][i] != color:
            temp += 1  # 경계점이 아니고 반대 색을 만나면 그 숫자를 센다.
    for j in range(y - 1, y - 1 - temp, -1):
        osello[x][j] = color
    return


def right(x, y, color):  # 착수점으로부터 오른쪽
    if y == N - 1: return  # 오른쪽 경계에 놓았으면 끝낸다.
    temp = 0
    for i in range(y + 1, N, +1):
        if osello[x][i] == color:
            break
        elif i == N - 1 or osello[x][i] == 0:
            return
        elif osello[x][i] != color:
            temp += 1
    for j in range(y + 1, y + 1 + temp, +1):
        osello[x][j] = color
    return


def up(x, y, color):  # 위
    if x == 0: return  # 위쪽 경계에 놓았으면 끝낸다.
    temp = 0
    for i in range(x - 1, -1, -1):
        if osello[i][y] == color:
            break
        elif i == 0 or osello[i][y] == 0:
            return
        elif osello[i][y] != color:
            temp += 1
    for j in range(x - 1, x - 1 - temp, -1):
        osello[j][y] = color
    return


def down(x, y, color):  # 아래
    if x == N - 1: return  # 아래쪽 경계에 놓았으면 끝낸다.
    temp = 0
    for i in range(x + 1, N, +1):
        if osello[i][y] == color:
            break
        elif i == N - 1 or osello[i][y] == 0:
            return
        elif osello[i][y] != color:
            temp += 1
    for j in range(x + 1, x + 1 + temp, +1):
        osello[j][y] = color
    return


def d1(x, y, color):  # 대각선 왼쪽 위
    if x == 0 or y == 0: return
    temp = 0
    for i in range(N):
        if osello[x - i][y - i] == color:
            break
        elif (x - i == 0 or y - i == 0) or osello[x - i][y - i] == 0:
            return
        elif osello[x - i][y - i] != color:
            temp += 1
    for j in range(temp):
        osello[x - j][y - j] = color
    return


def d2(x, y, color):  # 대각선 오른쪽 아래
    if x == N - 1 or y == N - 1: return
    temp = 0
    for i in range(N):
        if osello[x + i][y + i] == color:
            break
        elif (x + i == N - 1 or y + i == N - 1) or osello[x + i][y + i] == 0:
            return
        elif osello[x + i][y + i] != color:
            temp += 1
    for j in range(temp):
        osello[x + j][y + j] = color
    return


def d3(x, y, color):  # 대각선 오른쪽 위
    if x == 0 or y == N - 1: return
    temp = 0
    for i in range(N):
        if osello[x - i][y + i] == color:
            break
        elif (x - i == 0 or y + i == N - 1) or osello[x - i][y + i] == 0:
            return
        elif osello[x - i][y + i] != color:
            temp += 1
    for j in range(temp):
        osello[x - j][y + j] = color
    return


def d4(x, y, color):  # 대각선 왼쪽 아래
    if x == N - 1 or y == 0: return
    temp = 0
    for i in range(N):
        if osello[x + i][y - i] == color:
            break
        elif (x + i == N - 1 or y - i == 0) or osello[x + i][y - i] == 0:
            return
        elif osello[x + i][y - i] != color:
            temp += 1
    for j in range(temp):
        osello[x + j][y - j] = color
    return


################## 여기서부터 nontrivial한 함수와 실행부#########################

def game(M):
    """
    inp를 읽어들여 osello 판을 채운다.
    위에서 정의한 8가지 함수를 이용한다.
    """
    for i in range(M):  # 착수점을 오셀로에 업데이트
        osello[inp[i][0]][inp[i][1]] = inp[i][2]

        # 기존의 오셀로 판의 흑/백을 잡아먹자!
        right(inp[i][0], inp[i][1], inp[1][2])
        left(inp[i][0], inp[i][1], inp[1][2])
        up(inp[i][0], inp[i][1], inp[1][2])
        down(inp[i][0], inp[i][1], inp[1][2])

        d1(inp[i][0], inp[i][1], inp[1][2])
        d2(inp[i][0], inp[i][1], inp[1][2])
        d3(inp[i][0], inp[i][1], inp[1][2])
        d4(inp[i][0], inp[i][1], inp[1][2])

    black = 0
    white = 0
    for j in range(N):
        for l in range(N):
            if osello[j][l] == 1:
                black += 1
            elif osello[j][l] == 2:
                white += 2
    print("%d %d" % (black, white))  # 출력까지 마무리하고 함수를 빠져나온다.
    return


########################### 여기서부터 main 실행부이다.
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    osello = [[0] * N for _ in range(N)]
    inp = [list(map(int, input().split())) for _ in range(M)]  # 착수점을 이중 리스트 input으로 저장
    if N == 6:  ######오셀로판 초기화하기
        osello[2][2] = 2
        osello[3][3] = 2
        osello[2][3] = 1
        osello[3][2] = 1
    elif N == 4:
        osello[1][1] = 2
        osello[2][2] = 2
        osello[1][2] = 1
        osello[2][1] = 1
    elif N == 8:
        osello[3][3] = 2
        osello[4][4] = 2
        osello[3][2] = 1
        osello[2][3] = 1

    print("#%d" % tc, end=" ")
    game(M)