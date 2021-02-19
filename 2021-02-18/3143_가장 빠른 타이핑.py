import sys
sys.stdin = open("sample_input (2).txt", "r")


def typying(s1, s2):
    cnt = 0
    origin_s1 = len(s1)
    i = 0
    while i <= len(s1)-len(s2):
        if s1[i:i + len(s2)] == s2:
            cnt += 1
            i += len(s2)
        else: i += 1
    result = origin_s1 - len(s2) * cnt + cnt

    return result


T = int(input())
for tc in range(1, T + 1):
    s1, s2 = map(str, input().split())
    print("#%d %d" %(tc, typying(s1, s2)))
