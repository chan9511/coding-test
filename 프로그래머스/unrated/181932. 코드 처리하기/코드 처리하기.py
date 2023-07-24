# 문제이해 및 요약.
# code 를 처리하는데, for문으로 가정하면 len(code)를
# 반복문으로 i 값을 idx 로 가정할 수 있다.
# 일단 첫번째 조건은 mode 가 0일 때, 1일 때이다.
# mode = 0 이면, i가 짝수값이면 ret 의 맨뒤에 code(i)를 append 해준다.
# mode = 1 이면, i가 홀수값이면 ret 의 맨뒤에 code(i)를 append 해준다.

# code[idx]가 "1"이 나온다면 모드는 변경된다. 
# ex) mode = 0 -> 1 , mode = 1 -> 0

# 그리고 마지막 조건으로 append를 담아주는 ret 이
# 빈 문자열이면 "EMPTY"를 리턴해준다.
def solution(code):
    mode = True
    ret = ''
    for idx, val in enumerate(code):
        if mode:
            # mode = 0
            if val != '1' and idx % 2 == 0:
                ret = ret + val
            elif val == '1':
                mode = False         
        else:
            # mode = 1
            if val != '1' and idx % 2 != 0:
                ret = ret + val
            elif val == '1':
                mode = True
    if len(ret) == 0:
        return 'EMPTY'            
    return ret