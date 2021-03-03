import sys
sys.stdin = open("sample_input (2).txt", "r")

T = int(input())
for tc in range(1, T+1):
    P = str(input())
    Q = str(input())
    if P == Q: ans = "N"
    elif P + "a" == Q: ans = "N"
    else: ans = "Y"
    print("#%d %s" % (tc, ans))

    # manaa
