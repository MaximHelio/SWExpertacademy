import sys
sys.stdin = open("input (9).txt", "r")

T= int(input())
for tc in range(1, T+1):
    thirtyone = [1, 3, 5, 7, 8, 10, 12]
    thirty = [4, 6, 9, 11]
    twentyeight = [2]
    date = str(input())

    if int(date[4:6]) in thirtyone:
        if 1 <= int(date[6:8]) <= 31:
            print(date[0:4] + '/' + date[4:6] + '/' + date[6:8])
        else: print("-1")

    elif int(date[4:6]) in thirty:
        if 1 <= int(date[6:8]) <= 30:
            print(date[0:4] + '/' + date[4:6] + '/' + date[6:8])
        else: print("-1")

    elif int(date[4:6]) in twentyeight:
        if 1 <= int(date[6:8]) <= 28:
            print(date[0:4] + '/' + date[4:6] + '/' + date[6:8])
        else: print("-1")
    else: print("-1")