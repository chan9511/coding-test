def solution(s):
    answer = ''
    # 쪼갠거 담아주고
    splinter = s.split(' ')
    # 쪼갠거 각각 내장함수로 처리해줌
    for i in range(len(splinter)):
        splinter[i] = splinter[i].capitalize()
        answer = ' '.join(splinter)
    return answer