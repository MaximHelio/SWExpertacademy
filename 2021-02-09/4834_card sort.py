import sys
sys.stdin = open("sample_input (4).txt", "r")


T = int(input())
for tc in range(1, T+1):
    # N: 카드의 개수
    N = int(input())
    num = str(input())
    arr = []
    for i in range(len(num)):
       arr.append(int(num[i]))
    print(arr)



    # 카드 숫자 세기
    # for i in num:
    #     cnt[int(i)] += 1
    # for i in range(len(cnt)) :
    #     # 이곳에 등호가 들어간 이유를 잘 생각해보자
    #     if max_cnt <= cnt[i]:
    #         max_num = i
    #         max_cnt = cnt[i]
    # print("#{} {} {}" .format(tc, max_num, max_cnt))
    #
    # for i in range(N):
    #     if Ai[i] in cnt_arr: cnt_arr[i] +=1
    #     else: cnt_arr[i] += Ai[i]
    # print(cnt_arr)



#
#     cntV = [0] * 10
#     # 1번
#     for i in range(len(Ai)):
#         pos = Ai[i]
#         cntV[pos] = cntV[pos] + 1
#
#     #변수명 주의
#     # 2번
#     for pos in Ai:
#         cntV[pos] = cntV[pos] + 1

