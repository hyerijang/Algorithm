# 무인도 
# 상하좌우로 연결된 땅은 하나의 무인도이다.
from collections import deque

def bfs(start,maps,visited):
    q = deque()
    q.append(start)
    y,x = start
    visited[y][x] = True
    result = []
    
    while q:
        y,x  = q.popleft()
        visited[y][x] = True
        result.append(int(maps[y][x]))
       
        # - 상하좌우 검사
        dy = [0,0,1,-1]
        dx = [-1,1,0,0]

        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]

            if not(0 <= ny<len(maps) and 0 <= nx < len(maps[0])):
                continue
            
            if visited[ny][nx] or maps[ny][nx] == 'X':
                continue
                
            visited[ny][nx] = True
            
            q.append((ny,nx))

    return result
    
def solution(maps):
    
    # 1.maps를 이차원배열로 변환
    maps  = [list(m) for m in maps]
    # print(maps)
    
    # 2. 무인도 찾기
    visited = [[False for _ in range(len(maps[0]))] for _ in range((len(maps)))]
    answer = []
    
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            # 방문했거나 바다이면 pass
            if visited[y][x] or maps[y][x] == 'X':
                visited[y][x] = True
                continue
                
            # 처음 방문한 육지인경우 bfs
            result = sum(bfs((y,x),maps, visited))
            answer.append(result)
    
    answer.sort()
    if not answer :
        answer = [-1]
    
    return answer
