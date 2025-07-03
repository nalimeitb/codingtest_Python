def solution(spell, dic):
    answer = 0
    
    list1 = list()
    list2 = list()
    
    for i in dic :
        list1.append([])
    
    for i in range(len(dic)) :
        for k in spell :
            if k in dic[i] :
                list1[i].append(0)
            else :
                list1[i].append(1)
                
    for i in list1 :
        list2.append(sum(i))
        
    if 0 in list2 :
        answer = 1
    else :
        answer = 2
    
    return answer