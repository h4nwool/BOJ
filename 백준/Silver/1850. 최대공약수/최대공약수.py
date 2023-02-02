import math
a, b = map(int, input().split())

answer = math.gcd(a,b)
print('1' * answer)