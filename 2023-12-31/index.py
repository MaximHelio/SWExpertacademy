# 고르마의 마지막 정리
i = 1
current = 1
add = 1

while i < 5:
    print(current)
    add += 1
    current = int(str(current) + str(add))
    i += 1
