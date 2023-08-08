def solution(n):
    answer = []
    for i in range(n+1):
        if i == 0:
            answer.append(i)
        elif i == 1:
            answer.append(i)
        else:
            plus = answer[i-1] + answer[i-2]
            answer.append(plus % 1234567)

    return answer[-1]