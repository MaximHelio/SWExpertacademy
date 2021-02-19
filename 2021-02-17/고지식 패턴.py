def BruteForce2(p,t):
    N = len(t)
    M = len(p)

    # 시작 위치를 컨트롤
    for i in range(N-M+1):
        cnt = 0
        for j in range(M):
            if t[i+j] == p[j]:
                cnt += 1
            else: break
        if cnt ==M