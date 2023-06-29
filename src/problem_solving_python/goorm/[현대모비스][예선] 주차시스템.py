# 테케 2개 타임아웃 남

from collections import deque

n, m  = map(int, input().split()) # 세로, 가로
parking = []

for _ in range(n):
	tmp = list(map(int, input().split()))
	parking.append(tmp)
	
# 미방문 : -1
# 주차함 : 0
# 구역번호 1 ~
visited= [[-1 for x in range(m)] for y in range(n)]
		
# 상하좌우로 이동
dy = [-1,1,0,0]
dx = [0,0,-1,1]


def get_score(y,x):
	if parking[y][x] == 2:
		return -2
	elif parking[y][x] == 0:
		return 1
	else:
		print("XXXXXX")
		return 0
	
#DFS
idx = 0
score = [0]
def dfs(y,x):
	# 비어있는 구역인 경우 탐색 시작
	global idx
	idx +=1  # 구역 번호
	score.append(0)
	stack = [(y,x)]
	
	while stack:
		y, x  = stack.pop()
		visited[y][x] = idx
		score[idx]+= get_score(y,x)
		
		for i in range(4):
			ny,nx = y+dy[i], x+dx[i]
			
			if not(0<= ny < n and 0<= nx< m):
				continue
				
			if visited[ny][nx] >= 0: # 방문
				continue
				
			if parking[ny][nx] == CAR:
				visited[ny][nx] = 0 # 차 있음
				continue
				
			stack.append((ny,nx))
			visited[ny][nx] = idx
				
			


	
for y in range(n):
	for x in range(m):
		if parking[y][x] == 1:
			visited[y][x] = 0 # 차 있음
			continue
		if visited[y][x] >= 0: # 방문
			continue
			
		dfs(y,x)
			
print(max(score))

	
	
