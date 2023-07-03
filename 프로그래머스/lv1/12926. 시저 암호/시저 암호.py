def solution(s, n):
    small = "abcdefghijklmnopqrstuvwxyz" 
    big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # 알파벳은 26개씩 싸이클
    answer = ''
    for i in s:
        if i in small:  # s에 소문자가 들어왔을 때
            answer += small[(small.find(i) + n)%26] # find함수는 string.find(찾을 문자)
        elif i in big:  # s에 대문자가 들어왓을 때
            answer += big[(big.find(i) + n)%26]
        else: # 공백을 포함하고 있을 때
            answer += ' ' # 공백추가
    return answer