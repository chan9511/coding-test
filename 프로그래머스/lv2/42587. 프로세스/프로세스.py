from collections import deque

def solution(priorities, location):
    # 큐로 치환
    que = deque(priorities) 
    answer = 0
    # 큐
    while que:
        big = max(que)
        save = que.popleft()
        location -= 1 
        if save != big:
            que.append(save)
            if location < 0:
                location = len(que) -1
        else:
            answer += 1
            if location < 0:
                break
            
    return answer