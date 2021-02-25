import sys
sys.stdin = open("input (1).txt", "r")

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [[0] * N for _ in range(N)]
#     result = str()
#     for i in range(N):
#         for j in range(i+1):
#             if j == 0 or j == i: arr[i][j] = 1
#             elif i == 1: arr[i][j] = 1
#             elif i > 1 and j >= 1: arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
#     print("#%d" %(tc))
#     for i in range(N):
#         for j in range(len(arr[i])):
#             if arr[i][j] != 0:
#                 print(arr[i][j], end = " ")
#         print()

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     result = []
#         for i in range(1, N+1):
#             tmp = []
#             for j in range(i):
#                 if j == 0 or j == i-1:
#                     tmp.append(1)
#             else: tmp.append(result[i-2][j-1] + result[i-2][j])
#             result.append(tmp)
#         string = ''
#         for i in range(N):
#             string += ' '.join(map(str, result[i])) + '\n'
#         print('#{} \n{}'.format(tc, string[:-1]))

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [1]
#
#     print('#{}'.format(tc))
#     for i in range(N):
#         print(*arr)
#         temp1 = arr[:]
#         temp2 = arr[:]
#         temp1.append(0)
#         temp2.insert(0, 0)
#         arr = [temp1[i] + temp2[i] for i in range(len(temp1)]

def pascal(N, arr):
    if len(arr) > N: return
    print(*arr)
    arr.append(0)
    arr.insert(0, 0)
    arr_new = []
    for i in range(len(arr)-1):
        arr_new.append(arr[i]+arr[i+1])
    pascal(N, arr_new)

    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [1]
    print("#%d" %tc)
    pascal(N, arr)
