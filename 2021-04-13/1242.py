import sys
sys.stdin = open('input (20).txt', 'r')

conversion = {'0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3',
          '0100011': '4', '0110001': '5','0101111': '6', '0111011': '7',
          '0110111': '8', '0001011': '9'}

def authen(arr, j):
    code = str()
    num = 0
    for k in range(8):
        p = conversion[arr[j - 7:j]]
        code = code + p
        # 짝수일 때 3배
        if k % 2:
            num += int(p) * 3
        # 홀수
        else: num += int(p)
        j -= 7
    if not num % 10:
        sum = 0
        for c in code:
            sum += int(c)
        return sum
    return 0


def chk():
    for i in range(n):
        for j in range(m - 1, -1, -1):
            if data[i][j] == '1':
                # 암호문 있는 행의 정보_arr/열 반환
                return authen(data[i], j + 1)


for tc in range(1, int(input()) + 1):
    # 세로: n, 가로: m
    n, m = map(int, input().split())
    data = list(input() for _ in range(n))
    # print(data)
    print('#%d %d' %(tc, chk()))
