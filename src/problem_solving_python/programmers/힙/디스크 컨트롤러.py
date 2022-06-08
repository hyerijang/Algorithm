
import heapq

def solution(jobs):
    logs = []
    
    # job :  [작업이 요청되는 시점, 작업의 소요시간] 
    jobs.sort()# 요청되는 시점이 빠르고, 소요시간이 짧은 순으로 정렬
    
    time = 0
    ready = []
    visited = [False for _ in range(len(jobs))]
    
    done = 0
    
    while len(logs) != len(jobs):
        # 1. 다음 작업이 될 수 있는 작업들을 ready 에 넣는다.
        for idx , job in enumerate(jobs):
            요청시점, 소요시간 = job
            if not visited[idx] and 요청시점 <= time:
                heapq.heappush(ready,[소요시간, 요청시점]) # 힙안에는 [소요시간, 요청되는 시점]
                visited[idx] = True
                
        # 1.1 지금 당장 준비된 작업이 하나도 없다면
        # 먼저 요청이 들어온 애부터 처리
        if not ready:
            idx = visited.index(False)
            요청시점, 소요시간 = jobs[idx]
            heapq.heappush(ready,[소요시간, 요청시점]) # 힙안에는 [소요시간, 요청되는 시점]
            visited[idx] = True
            time = 요청시점 # 갱신!!!!
            
        # 2. 작업을 1개 처리한다.
        # 기준 : reday에서 소요시간이 가장 짧은 것. 
        job = heapq.heappop(ready)
        소요시간 , 요청시점 = job
        time += 소요시간 #작업끝난시간
        logs.append(time - 요청시점) # 요청부터 종료까지 걸린시간 기록
    
    # 
    print(logs,jobs)
        
    return sum(logs)// len(logs)
