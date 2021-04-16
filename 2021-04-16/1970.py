# import sys
# sys.stdin = open('input (2).txt')

T = int(input())
lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, T+1):
    price = int(input())
    # 경우의 수 저장할 array
    result = [0] * len(lst)
    # 내림차순 이므로, 인덱스 별로 몫을 저장하면 그것이 최소 개수의 결과를 만듦
    for i in range(len(lst)):
        result[i] = price // lst[i]
        price = price % lst[i]

    print('#%d' %tc)
    for i in result:
        print(i, end=" ")
    print()