import sys
sys.stdin = open('sample_input (7).txt')

T = int(input())
for tc in range(1, T+1):
    val = float(input())
    a = 0.5
    cnt = 0
    result = []
    while val > 0 and cnt < 13:
        if val >= a:
            result.append('1')
            val -= a
        else:
            result.append('0')
        a = a*0.5
        cnt += 1
    if cnt == 13:
        ans = 'overflow'
    else:
        ans = ''.join(result)
    print('#%d %s' %(tc, ans))