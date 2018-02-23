# Uses Python3
import random

from maximumPairWaiseProduct import MaxPairWaiseProduct, MaxPairWaiseProductNaive, MaxPairWaiseProductTest

def stressTesting(N, M):
    while(True):
        n = random.randint(2, N)
        a = []
        for i in range(0, n):
            a.append(random.randint(1, M))
        print(a)
        result1 = MaxPairWaiseProduct(n, a)
        result2 = MaxPairWaiseProductNaive(n, a)
        result3 = MaxPairWaiseProductTest(n, a)

        if(result1 * 3 != result1 + result2 + result3):
            print('Wrong answer', result1, result2, result3)
            return
        
        print('OK', result1)

stressTesting(5, 10)