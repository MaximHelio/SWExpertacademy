T =int(input())
for tc in range(1, T+1):
    inp = list(input())
    inp.sort()
    answer = ''
    idx = 0
    while idx < len(inp) - 1:
        if inp[idx] == inp[idx+1]:
            idx += 2
        else:
            answer += inp[idx]
            idx += 1
    if len(inp) - 1 == idx: answer += inp[idx]

    if len(answer) > 0:
        print("#%d" % tc, end=" ")
        print(answer)
    else:
        print("#%d Good" % tc)
