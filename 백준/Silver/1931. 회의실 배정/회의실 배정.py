# 1931
n = int(input())
array = []

for i in range(n):
    a, b = list(map(int, input().split()))
    array.append((a,b))
    
array.sort(key = lambda x: x[0])
array.sort(key = lambda x: x[1])

count = 1
end = array[0][1]
for i in range(1, n):
    if array[i][0] >= end:
        count += 1
        end = array[i][1]
print(count)    