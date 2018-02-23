# Uses Python3
# Greatest divisor common
import sys

def GCDNaive(a, b):
    best = 0
    if(b == 0 or a == 0):
        return 0
    if(b > a):
        [a, b] = [b, a]
    for i in range(1, a + 1):
        if(a % i == 0 and b % i == 0):
            best = i
    return best

# Euclidean Algorithm
def EuclideanGCD(a, b):
    if b == 0:
        return a
    rem = a % b
    return EuclideanGCD(b, rem)

# Minimo multiplicados comum (O menor numero que "a" e "b" conseguem dividir)
def LeastCommonMultiple(a, b):
    gcd = EuclideanGCD(a, b)
    value1 = a // gcd
    value2 = b // gcd

    return value1 * value2 * gcd

input = sys.stdin.read().split()
a = int(input[0])
b = int(input[1])
print(LeastCommonMultiple(a, b))