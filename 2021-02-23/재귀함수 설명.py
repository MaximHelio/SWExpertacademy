def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

for i in range(2, 5):
    print(fib(i))

#1 1 2 3 5 8

K의 비트 스트링 중에서 1이 연속하지 않는 bit string
예) K = 4 0001, 0010, 1010
K = 1     0      1      2가지
K = 2    0   1   0      3가지
K = 3   0  1  0  0 1    5가지
K = 4  0 1 1 0 1 0 1 0  8가지

f(n) = f(n-1) + f(n-2)

파랑 1cm,  노랑 1cm, 빨강 2cm 의 종이를 갖고 Kcm를 만드는 방법
K=1      B        Y               2
K=2    B  Y     B  Y     R        5
K=3 B Y B Y R   B Y B Y  B Y R   12
K=4
f(n) = 2*f(n-1) + f(n-2)

문제)
K=1   1(세로)
K=2   1(세로)    1(가로2개)   2
K=3   1(세로)    1(세로)      1(세로)

f(n) = f(n-1) * 2f(n-2)