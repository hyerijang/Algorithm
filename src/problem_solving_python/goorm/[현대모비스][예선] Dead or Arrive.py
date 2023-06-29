# 정답
# 입력 다 받아서 정렬하는 것 보다는 그냥 하나씩 비교하는게 속도 빠름

# 같은 (속도) : 높은 내구도
# 같은 (속도, 내구도) : 높은 차량번호

n = int(input())

speed = dict() 
for cidx in range(1,n+1):
	v, w = map(int, input().split())
	
	if speed.get(v) == None:
		speed[v] = [w, cidx] # speed가 v일때  [내구도, 차량번호]
		continue
	
	# 내구도 더 높은경우
	if speed[v][0] < w:
		speed[v] = [w,cidx]
	
	# 내구도 같지만 차량번호 더 높음
	elif speed[v][0] == w :
		speed[v][1] =  max(speed[v][1], cidx)
		

answer = 0
for v in speed.keys():
	answer += speed[v][1]
print(answer)
