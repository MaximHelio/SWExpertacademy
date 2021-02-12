def prt(lst):
    tlst = lst[::]
    print('2:', tlst)
    tlst[0] = 100000
    print('2:', tlst)
    value = len(lst)
    return value

def prt1():
    p1 = [0] * 10

alst = [1, 2, 3, 4]
blst = [2, 1, 2, 3, 4]
clst = [3, 4, 5, 2, 1, 2, 3, 4]

print('1:', alst)
a = prt(alst)
print(a)
print(prt(alst))
prt(blst)
print('3:', alst)