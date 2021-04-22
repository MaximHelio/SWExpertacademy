def dij(s):
    D[s][0] = 0
    D[s][1] = 0

    for k in range(N+1):
        if i in range(N+1):
            if i in U: continue
            if D[i][0] < minV:
                curV = i
                minV = D[i][0]
    