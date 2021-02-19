import sys
sys.stdin = open("sample_input (4).txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(str(input())) for _ in range(N)]

    # 가로
    for i in range(N):
        for j in range(N-M+1):
            s_lst = []
            for k in range(M):
                s_lst.append(arr[i][j+k])
        if s_lst == list(reversed(s_lst)):
            joined_str = ''.join(s_lst)
    #세로
    for j in range(N):
        for i in range(N-M+1):
            s_lst = []
            for k in range(M):
                s_lst.append(arr[i+k][j])
        if s_lst == list(reversed(s_lst)):
            joined_str = ''.join(s_lst)

    print("#%d %s" %(tc, joined_str))

# 풀이
def my_reverse(line):
    r_line = []
    # 뒤에서부터 읽어오면서 뒤집은 리스트를 만들자!
    for i in range(len(line)-1, -1, -1):
        r_line.append(line[i])

    return r_line


def my_find():
    # 전체 크기가 N
    for i in range(N):
        # 가로 검사
        for j in range(N-M+1):
            # 부분 문자열을 위한 빈 리스트
            tmp = []
            # 부분 문자열 완성!!
            for k in range(M):
                tmp.append(words[i][j+k])
            # tmp = words[i][j:j+M]
            # 회문 검사
            if tmp == my_reverse(tmp)
                return tmp
        # ########################################
        # 세로 검사
        for j in range(N-M+1):
            tmp = []
            for k in range(M):
                tmp.append(words[j+k][i])
            # tmp = words[j:j+M][i] 세로일 땐 안나옴
            if tmp == my_reverse(tmp):
                return tmp
    # 문제에서 회문이 1개 존재한다고 하였으므로, 필요하지는 않음
    return = []


#테스트 케이스 입력
T = int(input())

for tc in range(1, T+1):
    # N : 2차원 리스트의 크기 10 <= n <= 100
    # M : 우리가 찾고 싶은 회문의 길이 5 <= M < N

    #리스트 내포 방식을 이용한 입력 처리
    words = [list(input()) for _ in range(N)]
    ans = my_find()

    print("#{} {}".format(tc, ''.join(ans)))
# for 문 이용해서 하는 거_