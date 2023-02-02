def solution(n):
    answer = 0
    a = int(n ** 0.5)
    if a ** 2 == (n ** 0.5) ** 2:
        answer = (a + 1) ** 2
    else:
        answer = -1
    return answer