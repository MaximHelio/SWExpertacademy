import sys
sys.stdin = open("1_input.txt", "r")

T =int(input())
for tc in range(1, T+1):
    inp = list(input())
    inp.sort()
    stack = []
    for letter in inp:
        if stack and stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)
    if stack:
        print("#%d %s" %(tc, i for i in stack))
    else:
        print("#%d 'GOOD'" %tc)



