T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    name_set = set()
    for i in range(N):
        name = input()
        name_set.add(name)
    name_list = list(name_set)

    name_list = sorted(name_list, key=len)
    name_list = sorted(name_list)

    print("#%d" % tc)
    for name in name_list:
        print(name)