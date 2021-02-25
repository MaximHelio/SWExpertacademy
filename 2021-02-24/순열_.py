arr = [5, 6, 7]
sel = [0] *N
visited = [False] *N
N = 3
def powerset(k):
    if k==N:
        for i in range(N):
            print(sel[i], arr[sel[i]])
    for i in range(N):
        if visited[i]: continue
        visited[i] = True
        sel[k] = i
        powerset(k+1)
        visited[i] = False

        for i in range(N):
            if visited & (1<<i):
                continue
            visited = visited | (1<<i)
            sel[k] = i
            powerset(k + 1, visited)

        v = xxxPxx & 1<<2
            & 000100
            p: 0 => 000000
            p: 1 => 000100
        v= xxxPxx | 1<<n
           000100
=> xxx1xx


    # sel[k] = 0
    # powerset(k+1)
    #
    # sel[k] = 1
    # powerset(k+1)