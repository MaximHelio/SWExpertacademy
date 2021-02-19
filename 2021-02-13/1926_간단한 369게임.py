N = int(input())
for num in range(1, N+1):
    cnt = 0
    result = str(num)
    i = 0
    while i < len(str(num)):
        if result[i] == str(3) or result[i] == str(6) or result[i] == str(9):
            cnt += 1
            i += 1

    if cnt != 0:
        result = "-" * cnt

    print(result, end=" ")

# N = int(input())
#
# game = '369'
# result = [''] * N
# for num in range(1, N + 1):
#     num_str = str(num)
#     for n in num_str:
#         if n in game:
#             result[num - 1] += '-'
#     if result[num - 1] == '':
#         result[num - 1] = num_str
# result_str = ' '.join(result)
# print(result_str)