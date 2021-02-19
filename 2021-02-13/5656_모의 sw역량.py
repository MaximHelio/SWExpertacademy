import copy


def f(n, k, W, H, org):
    global minV
    if n == k:
        cnt = 0
        for i in range(H):
            for j in range(W):
                if org[i][j] != 0:
                    cnt += 1
        if minV > cnt:
            minV = cnt
    elif minV == 0:
        return
    else:
        for i in range(W):
            dest = copy.deepcopy(org)

            crack(i, N, W, H, dest)
            f(n + 1, k, W, H, dest)


def crack(c, N, W, H, br):
    q = []
    r = 0
    while (r < H and br[r][c] == 0):
        r += 1
    if r == H:
        return
    q.append((r, c))
    while q:
        i, j = q.pop(0)
        k = br[i][j]
        br[i][j] = 0
        for dis in range(1, k):
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni = i + dis * di
                nj = j + dis * dj
                if 0 <= ni < H and 0 <= nj < W:
                    q.append((ni, nj))
    for k in range(W):
        st = []
        for j in range(H - 1, -1, -1):
            if br[j][k] != 0:
                st.append(br[j][k])
                br[j][k] = 0
        for j in range(0, len(st)):
            br[H - 1 - j][k] = st[j];


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    org = [list(map(int, input().split())) for _ in range(H)]
    minV = 100000000
    f(0, N, W, H, org)
    print(f'#{tc} {minV}')