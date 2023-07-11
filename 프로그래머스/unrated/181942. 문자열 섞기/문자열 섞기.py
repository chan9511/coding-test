def solution(str1, str2):
    answer = ''
    for i in range(0,len(str1)):
        answer = answer + str1[i] + str2[i]
    return answer


# 첫 풀이
# def solution(str1, str2):
#     if len(str1)==len(str2):
#         answer = (str1[0]+str2[0]) * len(str1)
#         return answer
        
        