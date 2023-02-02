import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    arr.append(a)

arr = sorted(arr)    
for i in sorted(arr, key=lambda x: x[1]):
    print(i[0], i[1])