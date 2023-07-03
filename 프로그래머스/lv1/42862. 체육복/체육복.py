def solution(n, lost, reserve):
    
      
    chajip_reserve = set(reserve) - set(lost) 
    chajip_lost = set(lost) - set(reserve) 
    
    for i in chajip_reserve:
        
        if i-1 in chajip_lost: # 여벌로 가지고 있는 학생이 앞쪽 없는 학생한테 주는 경우
            chajip_lost.remove(i-1)
        
        elif i+1 in chajip_lost: # 왼쪽을 충족시키고 뒷쪽 없는 학생한테 주는 경우
            chajip_lost.remove(i+1)
            
    return n - len(chajip_lost) # 전체 학생 수에서 다 빌려주고도 없는 학생들 빼기