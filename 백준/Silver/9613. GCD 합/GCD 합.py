import sys
import math

n=int(input())

for i in range(n):
    arr=list(map(int, sys.stdin.readline().split()))
    result = 0
    for j in range(1,len(arr)):
        for k in range(j + 1,len(arr)):
            result += math.gcd(arr[j],arr[k])

    print(result)