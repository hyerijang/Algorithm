# https://programmers.co.kr/learn/courses/30/lessons/43164
# 프로그래머스 Level 3
# 성공 (40분)
# 옛날에 코테 때 나왔던 문제 같은뎅?? 다시 풀어서 그런지 내가 발전한건지 쫌 쉬웠다. 

def solution(tickets):
    answer = []  
    graph = {}
    
    tickets.sort() # 미리 정렬
    for idx, t in enumerate(tickets):
        if not graph.get(t[0]):
            graph[t[0]] = []
        graph[t[0]].append(idx) 

    # print(graph)

    def dfs(graph:dict, used : list, route:list):       
        if len(route) == len(tickets) +1:
            print(answer)
            return route[:]
        
        start = route[-1]
        print(route)
        
        if not graph.get(start):
            return
        
        for next_idx in graph[start]:
            if not used[next_idx]:
                used[next_idx] = True
                route.append(tickets[next_idx][1])
                if dfs(graph, used, route):
                    return route # 종료조건 
                
                used[next_idx] = False
                route.pop()
                
        return
    
    used = [False for _ in range(len(tickets))]
    answer = dfs(graph,used,["ICN"])
    return answer
