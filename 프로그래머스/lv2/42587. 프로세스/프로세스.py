from collections import deque

def solution(priorities, location):
    # 큐로 치환
    que = deque(priorities) 
    answer = 0
    # location 안에 있는 프로세스처리
    while que:
        # que안에서 제일 큰 것(우선순위제일높은 것)
        big = max(que)
        # 맨앞이 우선순위가 아니면 따로 저장해주려고 save라 칭함
        save = que.popleft()
        location -= 1 
        # 빼준 것이 우선순위가 제일 높은 친구가 아니라면
        if save != big:
            # 다시 들어가!
            que.append(save)
            # 로케이션이 0이 되면 기다리던 숫자가 왔다고 볼 수 있지
            # 하지만 내가 바라던 숫자(location)이 차례가 안됐다면
            # 다시 뒤로 보내야하니, 그의 인덱스번호를 맨뒤번호로 설정해준다
            if location < 0:
                location = len(que) -1
        else:
            answer += 1
            if location < 0:
                break
            
    return answer