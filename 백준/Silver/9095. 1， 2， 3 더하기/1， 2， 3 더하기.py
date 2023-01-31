n = int(input())

d = [0] * 1001
d[0] = 1
d[1] = 2
d[2] = 4

for i in range(n):
    a = int(input())
    
    for j in range(3, 1001):
        d[j] = d[j - 3] + d[j - 2] + d[j - 1]
    
    print(d[a-1])