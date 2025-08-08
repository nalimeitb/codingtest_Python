def solution(strings, n):
    answer = []
#     list1 = list()
    
#     for i in strings :
#         list1.append(i[n]+i)
    
#     list1 = sorted(list1)
    
#     for i in list1 :
#         answer.append(i[1:])
    
    
    dict1 = {}
    dict2 = {}
    
    for i in strings :
        dict1[i] = i[n]
        
    for i in strings :
        dict1[i] = dict1[i] + i
    
    for x,y in dict1.items() :
        dict2[y] = x
        
    for x, y in sorted(dict2.items()) :
        answer.append(y)
        
    
    return answer