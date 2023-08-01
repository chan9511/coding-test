def solution(numbers):
    # answer에 -1을 numbers의 길이만큼 넣어주고
    answer = [-1] * len(numbers)
    # 빈 리스트에 stack이라 칭하고
    stack = []
    
    # numbers만큼 반복문을 돌려준다.
    for i in range(len(numbers)):
    
    # target은 하나하나 숫자를 나타냄.
        target = numbers[i]
        
        # stack과 numbers[stack의 맨 뒤에 수] 가 target 보다 작으면
        while stack and numbers[stack[-1]]<target:
            # answer[스택에서 나온숫자] 가 target이 된다.
            answer[stack.pop()]=target
            
            
        stack.append(i)
                
    return answer