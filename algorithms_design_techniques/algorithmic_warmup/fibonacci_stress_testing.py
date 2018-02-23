import fibonacci
import random

m = 10 # Maximo permitido

while(True):
    n = int(random.random() * m)
    naive = fibonacci.FibRecursNaive(n)
    fast = fibonacci.FibRecursFast(n)

    if(naive != fast):
        print('Wrong answer', naive, fast)
        return
    else:
        print('Ok')