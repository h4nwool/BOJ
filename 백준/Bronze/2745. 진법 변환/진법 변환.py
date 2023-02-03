n, b = input().split()
b = int(b)
n = ''.join(reversed(n))

arr  = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0

for i in range(len(n)-1, -1, -1):
    result += arr.index(n[i]) * (b ** i)

print(result)