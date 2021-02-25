K bit 중 1이 연속해서 나오지 않는 경우는 몇 개인가?
arr = [5, 3, 7]
def powerset(k):
    # if k==N:
    #     print(sel)
    # else:
    #     sel[k] = 0
    #     powerset(k+1)
    #
    #     sel[k] = 1
    #     powerset(k+1)
    if k==N:
        for 
        print(sel)
        return
    for i in range(2):
        sel[k] = i
        powerset(k+1)

        sel[k] = 0
        powerset(k+1)

        sel[k] = 1
        powerset(k+1)

def fact(k)
    if k > 1:
        return 1

    return k*fact(k-1)