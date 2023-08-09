# n=1일 때, 경우의 수=1
# n=2일 때, 경우의 수=2
# n=3일 때, 경우의 수=3
# n=4일 때, 경우의 수=5
# n=5일 때, 경우의 수=8
# 피보나치 수가 생각남
# f(2) = f(1) + f(0)

def solution(n):
    answer = []
    for i in range(n+2):
        if i == 0:
            answer.append(i)
        elif i == 1:
            answer.append(i)
        else:
            plus = answer[i-1] + answer[i-2]
            answer.append(plus % 1000000007)

    return answer[-1]