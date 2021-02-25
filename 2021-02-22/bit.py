T = int(input())
for tc in range(1, T+1):
    N, K =int(input().split())

    answer = 0
    for a in range(0, 4096):
        b = "{0:b}".format(a)
        b = '0'*(12-len(b)) + b
        cnt = 0
        for x in b:
            if x == '1': cnt += 1
        if cnt != 3: continue
        print(b)
        s = 0
        idx = 0
        for x in b:
            if x == '1':
                s += idx + 1
            idx += 1
        print(s)
        if s == K: answer += 1
    print("#%d %d" %(tc, answer))