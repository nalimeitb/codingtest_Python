def solution(participant, completion):
    answer = ''
    
    # 7차시도
    dic = dict()
    
    for i in participant :
        dic[i] = dic.get(i, 0) + 1
    
    for i in completion :
        dic[i] = dic[i] - 1
            
    for i in dic :
        if dic[i] != 0 :
            answer = i
            break
    
    # 6차시도
    # if len(set(participant)) != len(set(completion)) :
    #     for i in participant :
    #         if i not in completion :
    #             answer = i
    #             break
    # else :
    #     for i in participant :
    #         if participant.count(i) == 2 :
    #             answer = i
    #             break
    
    # 5차시도
#     dic = dict()
    
#     for i in participant :
#         dic[i] = dic.get(i, 0) + 1
    
#     for i in participant :
#         if i not in completion :
#             answer = i
#             break
            
#     if answer == '' :
#         for i in dic :
#             if dic[i] == 2 :
#                 answer = i
#                 break
            
    
    #4차시도
#     for i in dic :
#         if i in completion :
#             dic[i] = dic[i] - 1
            
#     for i in dic :
#         if dic[i] != 0 :
#             answer = i
#             break
    
    # for a, b in dic.items() :
    #     if a
    #     if b == 2 :
    #         answer = a
    #         break
    
    #3차시도
#     for i in participant :
#         if i in dic :
#             dic[i] = dic[i] + 1
#         elif i not in dic :
#             dic[i] = 1
    
#     for i in dic :
#         if i in completion :
#             dic[i] = dic[i] - 1
            
#     for i in dic :
#         if dic[i] != 0 :
#             answer = i
#             break
    
    #2차시도
#     list1 = participant.copy()
    
#     for i in participant :
#         if i in completion :
#             list1.remove(i)
            
    # answer = list1[0]
    
    #1차시도
    
#     for i in participant :
#         if participant[0] in completion :
#             participant.pop(0)
            
#     answer = participant[0]

    
    return answer