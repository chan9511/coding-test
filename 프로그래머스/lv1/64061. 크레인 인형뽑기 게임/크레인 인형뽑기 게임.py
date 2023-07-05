def solution(board, moves):
    baguni = [] # 인형을 담을 바구니.
    n = len(board)
    answer = 0
    for i in moves: # board 안에 moves가 가르키고 있는 열을 들어간다.
        for j in range(n): 
            if board[j][i-1] != 0: # 0이 아닌 것을 바구니에 담아준다.
                baguni.append(board[j][i-1])
                board[j][i-1] = 0 # 인형을 뽑은 자리는 0으로 바꿔주기.
                break
                
        if len(baguni) > 1: # 2개 이상 바구니에 있으면
            if baguni[-1] == baguni[-2]: # 마지막 두 수가 같다면
                    baguni.pop(-1)    # 그 2개를 펑
                    baguni.pop(-1)    
                    answer += 2       # 2개 터졌다고 보고
            
    return answer
                    