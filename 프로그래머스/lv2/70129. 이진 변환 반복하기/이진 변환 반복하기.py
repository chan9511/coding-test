# return 값은 몇 회 이진 변환을 가하는가, 이진 변환을 하면서 0을 몇 개를 제거했냐.
# 
def solution(s):
    answer = []
    # 이진 변환 횟수
    cnt = 0
    # 0의 개수를 세어줄 cnt0
    cnt0 = 0
    # s 가 1 이 될 때까지 슈웃~
    while True:
        # '1' 말고 1 넣어서 시간초과떠서 살떨림;
        if s == '1':
            break;
            
        # s 안에 0 개수 세기    
        cnt0 += s.count('0')
        # 0 인 것을 공백으로 변환하기
        s = s.replace('0','')
        # 이진수로 변경하기
        s = bin(len(s))[2:]
        
        cnt += 1
    # return 값은 몇 회 이진 변환을 가하는가 = cnt
    # 제거할 0의 개수 = 제거한 0 의개수
    answer = [cnt,cnt0]
    return answer