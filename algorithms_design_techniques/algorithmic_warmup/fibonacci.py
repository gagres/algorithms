# Uses Python3
import sys

def FibRecursNaive(n):
    if(n <= 1):
        return n
    return FibRecursNaive(n - 1) + FibRecursNaive(n - 2)

# Try using Big-O Notation
def FibRecursFast(n):
    f = [] # O(n)
    f.append(0) #O(1)
    f.append(1) #O(1)
    for i in range(2, n + 1): #O(n)
        f.append(f[i - 1] + f[i - 2]) #O(n)
    return f[n] #O(1)

def LastDigitFibonacci(n):
    f = [] # O(1)
    f.append(0) # O(1)
    f.append(1) # O(1)
    for i in range(2, n + 1): # O(n)
        f.append((f[i - 1] + f[i - 2]) % 10) # O(1)
    return f[n] # O(1)

def sumLastDigitFibNumbers(n):
    num1 = 0
    num2 = 1
    for i in range(2, n + 3):
        [num1, num2] = [num2, num1]
        num2 = (num1 + num2) % 10
    return num2 - 1

def FibDivisionModulus(n, m):
    f = [0, 1]
    seq_begin = 0
    seq_end = 2
    for i in range(2, n + 1):
        f.append((f[i - 1] + f[i - 2]) % m)
        if f[seq_begin] == f[i]:
            seq_begin += 1
        else:
            seq_end += 1 + seq_begin
            seq_begin = 0

        if seq_begin == seq_end:
            break

    if(seq_begin == seq_end):
        mod = n % seq_begin
    else:
        seq_end += seq_begin
        mod = seq_end - 1

    return f[mod]

input = sys.stdin.read().split()
n = int(input[0])
print(sumLastDigitFibNumbers(n))