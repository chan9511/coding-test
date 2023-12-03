# absolutes는 정수들의 절댓값을 담은 배열 / signs는 참,거짓을 판별해주고 sings가 참이라면 absolutes가 음,양으로 바뀌게 됨
# 같은 인덱싱의 signs의 값이 참이면 + 거짓이면 -를 붙인 정수를 다 더해주면 result 값이 나온다.
# 두 리스트의 길이가 같으므로 한 리스트의 길이만큼 for문을 돌면서 true면 더해주고 false면 빼줘서 다 연산된 값을 리턴한다.

def solution(absolutes, signs):
    answer =  0
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer
