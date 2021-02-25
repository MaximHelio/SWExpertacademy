# 반복문을 이용한 선형시간 O(n)
def Iterative_Power(x, n):
    result = 1

    for i in range(1, n+1):
        result *= x

    return result
# 분할 정복을 이용한 거듭제곱 O(logN)
def Recursive_Power(x, n):
    if n == 1: return x
    if n % 2 == 0:
        y = Recursive_Power(x, n//2)
        return y * y
    else:
        y = Recursive_Power(x, (n-1)//2)
        return y * y * x

#print(Iterative_Power(2, 200000))
print(Recursive_Power(2, 200000))