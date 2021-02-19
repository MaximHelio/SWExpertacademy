import sys
sys.stdin = open("sample_input (1).txt", "r")


def binSearch(key):
    first = 1
    last = P
    cnt = 0
    while first < last:
        center = (first + last) // 2
        if center == key:
            break
        elif center < key:
            first = center
        else:
            last = center
        cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    if binSearch(Pa) < binSearch(Pb): ans = "A"
    elif binSearch(Pa) > binSearch(Pb): ans = "B"
    else: ans = 0

    print("#%d %s" %(tc, ans))