# Uses Python3
def MaxPairWaiseProduct(n, a):
    index1 = 0
    for i in range(1, n):
        if(a[i] > a[index1]):
            index1 = i

    if index1 == 0:
        index2 = 1
    else:
        index2 = 0
    for i in range(1, n):
        if(i != index1 and a[i] > a[index2]):
            index2 = i
    return a[index1] * a[index2]

def MaxPairWaiseProductNaive(n, a):
    product = 0
    for i in range(0, n):
        for j in range(0, n):
            if(i != j and (a[i] * a[j]) > product):
                product = a[i] * a[j]
    return product

def MaxPairWaiseProductTest(n, a):
    n1 = 0
    n2 = 0
    for i in range(0, n):
        if(a[i] >= n1):
            [n1, n2] = [n2, n1]
            n1 = a[i]
        elif a[i] > n2:
            n2 = a[i]
    return n1 * n2
            