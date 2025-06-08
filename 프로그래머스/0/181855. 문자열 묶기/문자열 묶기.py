def solution(strArr):
    answer = 0
    counts = dict()
    
    for strs in strArr :
        if len(strs) not in counts :
            counts[len(strs)] = 1
            
        elif len(strs) in counts :
            counts[len(strs)] = counts[len(strs)] + 1
    
    answer = max(counts.values())
    
    
    
#     list1 = list()
    
#     for i in range(len(strArr)) :
#         if len(strArr[i]) not in list1 :
#             list1.insert((len(strArr[i])-1), 1)
            
#         elif len(strArr[i]) in list1 :
#             list1[(len(strArr[i])-1)] = list1[(len(strArr[i])-1)] + 1
    
#         print(list1)
#     answer = max(list1)
            
    
#시행착오2     list1 = list()
#     list2 = list()
    
    
#     for i in strArr :
#         list1.append(len(i))
        
#     print(list1)
    
#     for j in list1 :
#         list2.append(list1.count(j))
#     print(list2)
        
#     answer = max(list2)
    
    
#시행착오1     dic = {}
    
#     for i in strArr :
#         print(i)
#         print(len(i))
#         print(dic[len(i)])
#         if i not in dic :
#             dic[len(i)] = 1
#         else :
#             dic[len(i)] = dic[len(i)] + 1
        
#     print(dic)
    
    return answer