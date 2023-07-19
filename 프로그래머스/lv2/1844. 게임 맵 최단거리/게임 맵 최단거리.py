# 본인출발지점 (1,1) 예:(map[0][0]), 도착지점은 (n,m) 예:(map[4][4]) or (map[-1][-1])
# 하지만 (n,m)까지 길이 없으면 return -1
# 0은 벽이 있는 자리, 1은 벽이 없는 자리 map은 0과 1로만 이루어짐.
# 1이 있어야 경로진행가능.
# while answer == map[-1][-1]:
# visted는 생략. 주위둘러보고 1인 곳으로 이동
# 까지 찾게끔. 못찾으면 return answer = -1
# 찾았다면 그만큼의 경로 (이동한 횟수) return answer =  

from collections import deque
def solution(maps):
    answer = 0

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        # queue가 빌 때까지 반복
        while queue:
            x, y = queue.popleft()

            # 상하좌우 칸 확인하기
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 맵을 벗어나면 무시하기
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): continue

                # 벽이면 무시하기
                if maps[nx][ny] == 0:  continue

                # 처음 지나가는 길이면 거리계산하고 다시 상하좌우 확인하기
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))    # 재귀

        # 상대 팀 진영(제일 오른쪽 아래 칸)까지의 거리 반환
        return maps[len(maps)-1][len(maps[0])-1]

    answer = bfs(0, 0)
    return -1 if answer == 1 else answer    # 상대 팀 진영에 도착할 수 없을 때 -1

