def solution(progresses, speeds):
    answer = []
    b = 0
    while progresses != [] :
        a = 0
        progresses_1 = progresses[0]

        while progresses_1 < 100 :
            a = a + 1
            progresses_1 = progresses_1 + speeds[0]

        for i in range(len(progresses)) :
            progresses[i] = progresses[i] + speeds[i] * a
        
        
        answer.append(0)
        while progresses != [] and progresses[0] >= 100 :
            progresses.pop(0)
            speeds.pop(0)
            answer[b] = answer[b] + 1
            
        b = b + 1
            
        # print(progresses)
        # print(speeds)
        
#         answer.append(0)
#         answer[b] = 1
#         for i in progresses :
#             if i >= 100 :
#                 answer[b] = answer[b] + 1
#                 list1.append(progresses.index(i))
#             else :
#                 break

#         for i in list1 :
#             progresses.pop(i)
            
        # b = b + 1

            
    
    # if progresses[1] >= 100 :
        
        
    
#     list1 = list()
#     list2 = list()
    
#     answer.append(0)
#     for k in range(len(progresses)) :
#         if progresses[k] >= 100 :
#             answer[0] = answer[0] + 1
#         else :
#             list1.append(progresses[k])
#             list2.append(speeds[k])
    
#     b = 0
#     progresses_2 = list1[0]
    
#     while progresses_2 < 100 :
#         b = b + 1
#         progresses_2 = progresses_2 + list2[0]
        
#     for i in range(len(list1)) :
#         list1[i] = list1[i] + list2[i] * b
        
#     print(list1)
    
#     list3 = list()
#     list4 = list()
    
#     answer.append(0)
    
#     for j in range(len(list1)) :
#         if list1[j] >= 100 :
#             answer[1] = answer[1] + 1
#         else :
#             list3.append(list1[j])
#             list4.append(list2[j])
            
    
        
    
    # while len(progresses) != 0 :
        
    
    
#     progresses_1 = progresses.copy()
#     progresses_1.pop(0)
#     print(progresses)
#     print(progresses_1)
    
#     for i in range(len())
    
    return answer