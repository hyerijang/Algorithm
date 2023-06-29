# 노드 : (정비소) 1~N번
# 간선 : 양방향, 시작과 끝이 같은 정비소일 수 있다.
# ------------------------------------------------
# ! 차량은 모든 주행구간(간선)를 통과한 뒤 "1번 정비소로 돌아와야한다"
# 현재 주행 테스트로 가능하면 시설그대로 사용
# 안되면 최소 개수의 주행구간을 추가하여 시설을 사용 
# -------------------------------------------------
# 출력 : 조건 만족을 위해 추가해야하는 최소 주행구간의 개수
#-----------------------------------------------
# 모든 주행구간 "1번씩" 통과
# ----------------------------------------------

from collections import defaultdict, deque
from math import ceil
n, m = map(int,input().split())
정비소 = defaultdict(list)
for _ in range(m) :
	a,b = map(int, input().split())
	정비소[a].append(b)
	정비소[b].append(a)
	
odds = []
even = []
cmps = []
def dfs(start, visited, cmp):
	stack = [start]
	while stack:
		start = stack.pop()
		visited[start]  =  True 	# 방문표시	
		cmps[-1].append(start)

		if len(정비소[start])% 2 == 1 :
			# 간선이 홀수개인 경우
			odds[cmp].append(start)
		else:
			even[cmp].append(start)
	

		for next in 정비소[start]:
			if visited[next] == True:
				continue
			stack.append(next)

visited = [False] * (n+1)
visited[0] = True

cmp = 0 # 컴포넌트 번호
for start in 정비소.keys():
	if visited[start]:
		continue
	odds.append([])
	cmps.append([])
	even.append([])
	dfs(start,visited, cmp)
	cmp+=1
	
def choose(idx, odds, even):
	# 해당 컴포넌트에서 다른 컴포넌트와 연결할 노드 선택
	# 홀수 간선을 갖는 노드를 우선으로 하지만 없다면 짝수 간선을 갖는 노드를 선택한다.
	a = None
	if len(odds[idx]) == 0:
		a = even[idx].pop()
		odds[idx].append(a)
	else:
		a = odds[idx].pop()
		even[idx].append(a)
	return a

# 1. 모든 컴포넌트를 하나의 컴포넌트로 통합
answer = 0
while len(odds) > 1:
	# 첫번째 컴포넌트
	a = choose(0, odds,even)
	b = choose(1, odds,even)
	answer +=1
	odds.append(odds.pop()+odds.pop())
	even.append(even.pop()+even.pop())

	
# 통합된 컴포넌트 내에 홀수 간선 노드가 있다면 둘씩 연결짓는다
print(answer + len(odds[0])//2)

	
