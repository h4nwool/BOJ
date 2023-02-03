import sys

n, k = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
arr = sorted(arr)
print(arr[k-1])