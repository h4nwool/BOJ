import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    arr.append(a)
               
for i in sorted(arr):
    print(i[0], i[1])