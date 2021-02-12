import sys
sys.stdin = open("input (8).txt", "r")

def each_sum(N):
    sum = 0
    while N > 0 :
        rem = N % 10
        sum += rem
        N = N // 10
    return sum

N = int(input())
print(each_sum(N))