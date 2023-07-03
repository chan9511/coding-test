def solution(n):
    answer = []
    for x in range(2,n+1):
        if n % x == 1:
            answer.append(x)
    return min(answer)