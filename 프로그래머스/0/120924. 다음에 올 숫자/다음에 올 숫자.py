def solution(common):
    answer = 0
    list1 = list()
    a = len(common) - 1
    
    for i in range(len(common)-1, 0, -1) :
        list1.append(common[i] - common[i-1])
        
    if len(set(list1)) == 1 :
        answer = common[a] + (common[a] - common[a-1])
    else :
        answer = common[a] * (common[a] / common[a-1])
        
        
    return answer