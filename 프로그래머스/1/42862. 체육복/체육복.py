def solution(n, lost, reserve):
    answer = n - len(lost)
    list1 = list()
    list2 = list()
    list3 = list()
    
    for a in lost :
        for b in reserve :
            if a == b :
                list3.append(a)
                
    answer = answer + len(list3)
    
    for i in range(len(list3)) :
        if list3[i] in lost :
            lost.remove(list3[i])
            reserve.remove(list3[i])
    
    for i in lost :
        for k in reserve :
            if abs(i - k) == 1 :
                list1.append(i)
                list2.append(k)
    
    if len(set(list1)) < len(set(list2)) :
        answer = answer + len(set(list1))
    else :
        answer = answer + len(set(list2))

# def solution(n, lost, reserve):
#     answer = n - len(lost)
#     lost = sorted(lost)
#     reserve = sorted(reserve)
#     c_lost = lost.copy()
#     c_reserve = reserve.copy()
    
#     for i in c_lost :
#         for k in c_reserve :
#             if abs(i - k) <= 1 :
#                 answer = answer + 1
#                 c_reserve.remove(k)
#                 c_lost.remove(i)
#                 print(c_lost, c_reserve)
#                 break
            
#             else :
#                 print(c_lost, c_reserve)
            
#     return answer        
        
    
    return answer