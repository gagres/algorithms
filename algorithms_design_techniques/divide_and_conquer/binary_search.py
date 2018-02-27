import math
import sys

def BinarySearch(A, low, high, key):
    if high < low:
        return -1
    
    mid = int(math.floor((low + high) / 2))

    if(A[mid] == key):
        return mid
    
    if(key > A[mid]):
        return BinarySearch(A, mid + 1, high, key)
    else:
        return BinarySearch(A, low, mid - 1, key)

lines = sys.stdin.read().split('\n')

arr = lines[0].split(' ')

length = int(arr[0])
del arr[0]

search = lines[1].split(' ')
del search[0]

for value in search:
    print BinarySearch(arr, 0, length - 1, value),