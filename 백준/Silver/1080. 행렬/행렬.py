# 1080
N, M = map(int, input().split())
listA = [list(map(int, input())) for j in range(N)]
listB = [list(map(int, input())) for j in range(N)]
cnt = 0

def flip(i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            listA[x][y] = 1 - listA[x][y]


for i in range(N - 2):  
    for j in range(M - 2): 
        if listA[i][j] != listB[i][j]:
            flip(i, j)
            cnt += 1

        if listA == listB:
            break
    if listA == listB:
        break

if listA != listB:
    print(-1)
else:
    print(cnt)