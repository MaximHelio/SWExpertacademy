def fibo(n):
    # 해당 fibo가 얼마나 호출했는지 cnt시킴
    arr[n] += 1
    if n < 2:
        return n
    return fibo(n-1) +fibo(n-2)

# 호출횟수
arr = [0] * 35
print(fibo(20))

memo[0] -> 0으로
memo[1] -> 1로 초기화함

# 메모이제이션
def fibo1(n):
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1)+fibo1(n-2))
    return memo[n]

memo = [0,1]

print(fibo1(40))
print(memo)


#############################
memo2 = [-1] * 21
memo2[0] = 0
memo2[1] =1
def fibo2(n):
    if memo2[n] == -1:
        memo2[n] = fibo2(n-1) + fibo2(n-2)

    return memo2[n]

print(fibo2(10))
print(memo2)

DP(Dynamic Programming)
동적계획 알고리즘은 그리디 알고리즘과 같이 최적화문제를 해결하는 알고리즘이다
동적계획 알고리즘은 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로
