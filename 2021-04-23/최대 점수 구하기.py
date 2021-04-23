# 이번 정보올림피아드 대회에서 좋은 성적을 내기 위해 현수는
# 선생님이 주신 N개의 문제를 풀려고 한다.
# 각 문제는 그것을 풀었을 때 얻는 점수와 푸는 데 걸리는 시간이 주어지게 된다,.
# 제한 시간 M 안에 N개의 문제 중 최대 점수를 얻을 수 있도록 해야한다.
# 해당 문제는 해당 시간이 걸리면 푸는 걸로 간주한다. 한 유형 당 한 개만 풀 수 있다.
# 첫 번째 줄에 문제의 개수 N과 제한 시간 M이 주어진다.
# 두 번째 줄부터 N줄에 걸쳐 문제를 풀었을 때 얻는 점수와 푸는 데 걸리는 시간이 주어진다.
# 첫 번째 줄에 제한 시간 안에 얻을 수 있는 최대 점수를 출력한다.
def dfs(L, sum, total_time):
    global result
    # 가지치기
    if total_time > M:
        return
    if L == N: # 종착지점
        if sum > result:
            result = sum
    else: # 뻗어 나갔을 경우,
        dfs(L+1, sum+score[L], total_time+time[L])
        dfs(L+1, sum, total_time)


N, M = map(int, input().split()) # 총 문제의 개수, 제한 시간
score = []
time = []
for i in range(N):
    # 점수, 시간
    a, b = map(int, input().split())
    score.append(a)
    time.append(b)
result = -215000
dfs(0, 0, 0)
print(result)
