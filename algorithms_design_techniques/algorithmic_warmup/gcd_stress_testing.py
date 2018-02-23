import gcd
import random

m = 10 # Max numbers
while(True):
    a = int(1 + random.random() * m)
    b = int(1 + random.random() * m)

    naive = gcd.GCDNaive(a, b)
    fast = gcd.EuclideanGCD(a, b)

    if naive != fast:
        print('Wrong answer, parameters:', a, b, 'results:', naive, fast)
        break

    print('OK')
