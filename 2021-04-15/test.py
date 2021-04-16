def cal(lst):
    #012
    for i in range(len(lst)):
        s = lst[i]
        e = lst[i+1]
        sumV += arr[s][e]
    sumV = sumV + arr[e][0]
    return sumV

def perm(k, midV):
    global minV
    if minV < midV:
        return

    if k==N:
        midV = cal(lst)
        if minV > midV:
            minV = midV
        return

    for i in range(1, N):
        if not visited[i]:
            lst[k] = i
            visited[i] = True
            s =
            e = i
            perm(k+1, i, midV + arr[s][i])
            visited[i] = False

# 1231 => 0120
lst[0] = 0
visited[0] = True
perm(1)