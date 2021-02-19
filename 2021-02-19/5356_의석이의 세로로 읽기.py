import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = [str(input()) for _ in range(5)]
    len_arr = []
    for i in range(len(arr)):
        len_arr.append(len(arr[i]))
    max_len = max(len_arr)
    for i in range(5):
        if len(arr[i]) < max_len:
            for _ in range(max_len-len(arr[i])):
                arr[i] += " "
    result = str()
    for j in range(max_len):
        for i in range(5):
            result += arr[i][j]
    result = result.replace(" ","")
    print(result, type(result))

# 정석 풀이
T = int(input())
for tc in range(1, T+1):
    word = [0] * 5
    # 최대 길이를 담을 값
    max_len = 0
    for i in range(5):
        word[i] = list(input())
        if len(word[i]) > max_len:
            max_len = len(word[i])
    # 세로로 읽어보자.
    print("#{}".format(tc), end=" ")
    for i in range(max_len):
        for j in range(5):
            if len(word[j]) > i:
                print(word[j][i], end="")
            try:
                print(word[j][i], end="")
            except:
                pass
    print()