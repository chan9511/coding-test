# def solution(s):
#     answer = ''
#     for i in len(s):
#         if i % 2 == 0:
#             answer += s[i].upper()
#         else:
#             answer += s[i].lower()
        
#     return answer
def solution(s):
    answer = ''
    s = s.split(' ')
    for word in s:
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += ' '
    return answer[:-1]