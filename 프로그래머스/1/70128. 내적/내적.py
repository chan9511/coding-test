# 길이가 같은 a,b가 주어졌다.
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer