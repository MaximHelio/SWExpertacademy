Conversion = {'0':0,'1':1, '2':2, '3':3, '4':4,'5':5,'6':6,'7':7,'8':8, '9':9,
        'A':10,'B':11,'C':12, 'D':13,'E':14,'F':15}

def Binary(num):
    global result
    quo, rem = 0, 0
    for i in range(4):
        rem = num % 2
        result = str(rem) + result
        num = num // 2
    return

T = int(input())
for tc in range(1, T+1):
    N, decimal_num = map(str, input().split())

    ans = str()
    for i in decimal_num:
        result = str()
        Binary(Conversion[i])
        ans += result
    print('#%d %s'%(tc, ans))