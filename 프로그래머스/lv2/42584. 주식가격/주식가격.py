from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []
    
    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break 
        answer.append(sec)        
    return answer

# prices 값은 1 이상이어야 되고, 리스트의 길이는 2 이상.
# 가격이 변동이 아닌 가격이 떨어지지 않은 초(minute)을 리턴.
# 일단 return 값은 len(prices)보다 클 수 없다.
# 보기와 같이 len값이 5면 6초가 나올 수 없다. (길이+? 만큼 보기가 없기때문)
# 풀이설계
# prices 첫번째 인덱스 값을 확인한다.
# 두번째 인덱스 값을 확인한다. 두 값을 비교하여 첫 번째 인덱스보다 두 번째 인덱스 값이 크다면 +1 / 두번째 인덱스값이 작다면 +1
# answer말고 이 값만을 담아줄 리스트를 하나 더만듬(minute)
# 맨 앞을 pop해주고 마무리
# 그리고 남은 prices중 또 앞과 같은 방법으로 반복. 
# 리스트가 비게 된다면 반복문 종료 후
# minute을 정리해 answer로 변경
# return answer