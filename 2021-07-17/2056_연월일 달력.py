T = int(input())
for tc in range(1, T+1):
    date = str(input())
    if date[4:6] == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        if 0 < int(date[6:8]) <= 31:
            result = date[0:4] + '/' + date[4:6] + '/' + date[6:8]
    elif date[4:6] == 4 or 6 or 9 or 11:
        if 0 < int(date[6:8]) <= 31:
            result = date[0:4] + '/' + date[4:6] + '/' + date[6:8]
    elif date[4:6] == 2:
        if 0< int(date[6:8]) <= 28:
            result = date[0:4] + '/' + date[4:6] + '/' + date[6:8]
    else:
        result = -1
    print("#%d %s" %(tc, result))