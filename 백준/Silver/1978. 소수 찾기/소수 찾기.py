n = int(input())
arr = list(map(int, input().split()))
count = 0

if n == len(arr):
    for i in range(n):
        for j in range(2, arr[i] + 1):
            if arr[i] == j:
                count += 1
            if arr[i] % j == 0:
                break
                
print(count)