import sys
sys.stdin = open("sample_input (3).txt", "r")
########교수님 풀이#######
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split())) # 치즈량

    #화덕에 올라간 피자번호
    qlst = []
    for i in range(N):
        qlst.append(i)
    nextP = N

    while qlst:
        pizza = qlst.pop(0)
        cz = Ci[pizza]
        Ci[pizza] = cz // 2
        if cz //2 ==0:
            lstP = pizza
            if nextP < M:
                qlst.append(nextP)
        else:
            qlst.append(pizza)

    print("#%d %d" %(tc, lstP+1))