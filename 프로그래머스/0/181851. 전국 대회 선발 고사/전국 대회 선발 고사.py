def solution(rank, attendance):
    answer = 0
    list1 = list()
    dict1 = dict()
    
    for i in range(len(rank)) :
        if attendance[i] == True :
            dict1[rank[i]] = i
    
    list1 = sorted(dict1.items())
            
    answer = 10000 * list1[0][1] + 100 * list1[1][1] + list1[2][1]
        
            
    
    
#     for (i, k, v) in (range(len(rank)), rank, attendance) :
#         list1.append((i, k, v))
        
#     list1 = sorted(list1)
#     print(list1)
        
    
    
    return answer