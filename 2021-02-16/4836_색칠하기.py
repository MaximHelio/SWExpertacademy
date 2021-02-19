import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# T = 1 디버깅 위해 테스트
for tc in range(1, T+1):
    N = int(input())
    red_lst = []
    blue_lst = []
    for i in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if color == 1:
                    red_lst.append((x, y))
                elif color ==2:
                    blue_lst.append((x, y))
    common = []
    for grid in red_lst:
        if grid in blue_lst:
            common.append(grid)
    print("#%d %d" %(tc, len(common)))

# # 교수님 풀이
#     BRD = [[0] * 10 for _ in range(10)]
#     # BRD[1][1] = 1
#     # print(BRD)
#     for i in range(N):
#         r1, c1, r2, c2, color = map(int, input().split())
#         for r in range(r1, r2 + 1):
#             for c in range(c1, c2 + 1):
#                 BRD[r][c] += color
#     cnt = 0
#     if BRD[r][c] == 3:
#
# #2
#     def paint():
#         for r in range(stR, edR)