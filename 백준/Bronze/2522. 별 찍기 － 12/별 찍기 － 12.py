N = int(input())

for i in range(N):
    for j in reversed(range(N)):
        if i >= j:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
for i in range(N):
    for j in range(N):
        if j > i:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()