def solution(brown, yellow):
    
    answer = []
    # 문제를 잃어보면 결국 구해야하는건 노랑의 [가로,세로]
    yellow_x = 0 # 노랑의 가로
    yellow_y = 0 # 노랑의 세로
    
    for i in range(1, yellow+1) : # 노랑이 격자수는 1이상 이기에 1부터
        if yellow % i == 0 : # 1부터 노란색의 개수만큼 for문으로 반복하면서 노란색의 수가 i로
                             # 나누어 떨어지면 노란색의 가로는 노란색을 i로 나눈 몫이되고, 
                             #i는 노란색의 세로가 된다.
                             # 이때 위에서 언급한 수식을 사용하여 answer 리스트에
                             # yellow_x+2와 yellow_y+2를 넣어준다.
            yellow_x = int(yellow/i) 
            yellow_y = i
            if yellow_x*2 + yellow_y*2 + 4 == brown :            
                answer.append(yellow_x+2)
                answer.append(yellow_y+2)
                
                return sorted(answer, reverse = True)
    
    return answer