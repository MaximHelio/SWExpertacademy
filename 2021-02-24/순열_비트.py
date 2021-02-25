arr = [1, 2, 3]
N = 3
sel = [0] * N # 뽑은 결과를 적음

# check 10진수 정수
def perm(idx, check):
    if idx == N:
        print(sel)
        return

    for j in range(N):
        # j번째 원소를 활용을 했군, 그럼 쓰면 안되지
        if check & (1<<j): continue
        #     
        sel[idx] = arr[j]
        perm(idx+1, check | (1<< j)) # 원상복구가 필요 없다.

perm(0, 0) # 0번과 아무것도 가지지 않고있다는 의미
