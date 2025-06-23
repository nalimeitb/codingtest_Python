def solution(s):
    answer = ''
    dic1 = {}
    s = list(s)
    list1 = list()
    
    for i in s :
        dic1[i] = dic1.get(i, 0) + 1
        
    for k in dic1 :
        if dic1[k] == 1 :
            list1.append(k)
            
    list1 = sorted(list1)
    
    for i in list1 :
        answer = answer + i
    
    
    return answer