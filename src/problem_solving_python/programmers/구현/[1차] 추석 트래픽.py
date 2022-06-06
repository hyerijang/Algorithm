def get_start(end:tuple, t:float):
    
    
    day, hh, mm, ss = end
    
    # ㅂㅕㄴㅎㅗㅏㄴ
    ss = ss - t - 0.001
    
    if ss < 0:
        mm -= 1
        ss = 60 + ss
        
    if mm < 0:
        hh -= 1
        mm = 59
    
    if hh < 0:
        day -=1
        hh = 23
    
    start = (day,hh,mm,round(ss,3))
    return start

def solution(lines):
    answer = 0
    info = [] # start
    
    for log in lines:
        date, end, t = log.split() 
        
        #endtime translate
        end = end.split(sep=":")
        hh,mm = map(int,end[:-1])
        ss = float(end[-1])
        end = (15,hh,mm,ss)
        
        
        # T
        t = float(t[:-1]) 
         
        #starttime?
        start = get_start(end, t)
        # print(end, start)
        info.append((start,end))
    
    info.sort()
    
    
    START, END = 0, 1
    log_start = info[0][START]
    log_end = info[-1][END]
    
    # print(info)
    
    
    for idx, start_end in enumerate(info):
        start, end = start_end
        count = 0 
        for last_idx, last in enumerate(info):
            last_start , last_end = last
            if start < last_start:
                break
            
            tmp = get_start(start,1-0.003) #잘못 설계에서 이상하게 보정값이 들어가네
            if tmp < last_end:
                count+=1
            #     # print("O",tmp, last_end)
            # else :
            #     print("X",tmp)
    

        print(count)
        answer = max(answer, count)   
        
    return answer
