def solution(score):
    answer = []
    
    for i in range(len(score)) :
        score[i] = (score[i][0] + score[i][1]) / 2
        
    list1 = sorted(score.copy(), reverse = True)
    list2 = list()
    
    for i in range(len(score)) :
        list2.append(list1.index(score[i])+1)
        
    answer = list2   
    
    
    
    
    
    
    
    
    
#     list1 = list()
#     list2 = list()
#     list3 = list()
    
#     for x,y in score :
#         list1.append((x+y)/2)
        
#     list2 = list1.copy()
    
#     # print(list1)
    
#     for i in list1 :
#         list3.append(list1.index(max(list2)))
#         list2.remove(max(list2))
#         # print(list2)
#         # print(list3)
    
#     # for i in range(1, len(list3)) :
#     #     if list3[i] == list3[i-1] :
#     #         list3[i] = list3[i] + 1
            
#     print(list3)
    
#     list4 = list()
#     for i in score :
#         list4.append(0)
        
#     for i in range(len(list4)) :
#         if i >= 1 :
#             if list3[i] == list3[i-1] :
#                 list4[list3[i]] = i + 2
#             else :
#                 list4[list3[i]] = i + 1
#         else :
#             list4[list3[i]] = i + 1
        
#     answer = list4
    
    
    return answer