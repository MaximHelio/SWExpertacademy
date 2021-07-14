import sys
sys.stdin = open('input (9).txt')

T = int(input())
for tc in range(1, T+1):
    date = str(input())
    if 1<= int(date[4:6]) <= 12 and int(date[6:]) <= 28:
        print("#%d %s/%s/%s" %(tc, date[:4], date[4:6], date[6:]))
    else: print("#%d -1" %(tc))
