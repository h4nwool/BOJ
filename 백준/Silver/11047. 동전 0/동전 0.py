n, k = map(int, input().split())
count = 0
array = []

for i in range(n):
    a = int(input())
    array.append(a)



array.sort(reverse = True)


for coin in array:
    count += (k // coin)
    k %= coin
    
print(count)