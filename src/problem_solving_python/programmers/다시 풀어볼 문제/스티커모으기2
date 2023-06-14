#https://school.programmers.co.kr/learn/courses/30/lessons/12971

# 틀림 :  DP 방식으로 풀어야한다고 한다. 제대로 풀면 20줄 이내로도 가능. 
# 정답 코드 : https://latte-is-horse.tistory.com/231

import heapq

def 양옆(idx, sticker):
    left, right = idx-1, idx+1
    if left < 0: left = len(sticker) -1
    if right == len(sticker): right = 0
    return (left, right)

def 기회비용계산(idx, sticker):
    left, right = 양옆(idx, sticker)
    return sticker[left] + sticker[right]

   
def 기회비용변경(left, stidx, costlist, data, sticker, visited ):
    
    data[costlist[left]].remove(left)
    if len(data[costlist[left]]) == 0:
        del data[costlist[left]]

    # 영향받는 인덱스의 스티커가 이미 제거된 경우 종료 
    if visited[stidx]:
        return
    
    oldcost = costlist[stidx] 
    newcost = costlist[stidx] - sticker[left]
    
    # 기회비용이 이미 0인경우 갱신할 필요 없음
    if oldcost == 0:
        return
    
    # 이전 정보 제거
    data[oldcost].remove(stidx)
    if len(data[oldcost]) == 0:
        del data[oldcost]
    
    # 갱신된 정보 추가
    costlist[stidx] = newcost 
    if data.get(newcost) == None:
        data[newcost] = []
    data[newcost].append(stidx)
    

def 뜯어낼스티커찾기(li, sticker):
    target = li[0]
    
    for idx in li:
        if sticker[idx] > sticker[target]:
            target = idx
    
    return target

def solution(sticker):
    answer = 0
    data = dict()
    costlist = [0 for _ in range(len(sticker))]
    for idx in range(len(sticker)):
        cost = 기회비용계산(idx,sticker)
        costlist[idx] = cost
        if data.get(cost) == None:
            data[cost] = []
        data[cost].append(idx)

    visited = [False for _ in range(len(sticker))]
    
    while data:
        mincost = min(data.keys())
        # 뜯어낼 스티커 찾기
        target = 뜯어낼스티커찾기(data[mincost] , sticker)
        data[mincost].remove(target)
        # 코스트에 해당하는 인덱스 없으면 리스트 삭제
        if len(data[mincost]) == 0:
            del data[mincost]

        # 스티커 뜯는다
        visited[target] = True
        costlist[target] = 0
        answer += sticker[target]  # 떼넨 스티커
        
        # 스티커의 양옆은 찢어진다
        left, right = 양옆(target, sticker)
        # 때문에 왼쪽스티커의 왼쪽, 오른쪽스티커의 오른쪽은 기회비용이 변화함
        if not visited[left] :
            visited[left] = True
            ll = 양옆(left, sticker)[0]
            기회비용변경(left, ll, costlist, data ,sticker,visited)
            costlist[left] = 0
            
        if not visited[right] :
            visited[right] = True
            rr = 양옆(right, sticker)[1]
            기회비용변경(right, rr, costlist, data ,sticker,visited)
            costlist[right] = 0
            
    return answer
