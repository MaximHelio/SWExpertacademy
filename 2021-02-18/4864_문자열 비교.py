T = int(input())
for tc in range(1, T+1):
    s1 = str(input())
    s2 = str(input())
#     ans = 0
#
#     for i in range(len(s2)-len(s1)+1):
#         cnt = 0
#         for j in range(len(s1)):
#             if s2[i+j] == s1[j]:
#                 cnt +=1
#         if cnt == len(s1):
#             ans +=1
#
#     print("#%d %d" %(tc, ans)

# find 함수 이용
if str2.find(str1) != -1:
    ans =1
print("#{} {}".format(tc, ans))


# 브루트 포스 방법
def brute_force(p, t):

    for i in range(len(t)-len(p)+1):
        # 패턴의 길이만큼 반복
        is_ok = True # for else 구문이 생각나지 않을 때 변수를 활용
        for j in range(len(p)):
            if p[j] != t[i+j]:
                is_ok = False
                break
       # else: return 1

        if is_ok:
            return 1
    return 0
def brute_force2(p, t):
    i = 0 # 텍스트를 컨트롤하는 인덱스
    j = 0 # 패턴을 컨트롤하는 인덱스

    # j가 패턴의 길이가 된다면, 찾았다면 멈춘다.
    # i가 텍스트의 길이가 된다면, 멈춘다.
    while j < len(p) and i < len(t):
        if p[j] != t[i]:
            i = i-j # 시작 위치로 돌아가고
            j = -1
        i += 1
        j += 1
    # 패턴을 찾았다.
    if j == len(p): return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
# 보이어 무어도 작성해볼 것
# KMP도 해볼 것