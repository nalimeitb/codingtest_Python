def solution(arr):
    answer = 0
    list1 = []
    
    for i in range(len(arr)) :
        for j in range(len(arr[i])) :
            if arr[i][j] == arr[j][i] :
                list1.append(1)
            elif arr[i][j] != arr[j][i] :
                list1.append(0)
                
    if sum(list1) == 1 * len(list1) :
        answer = 1
    else :
        answer = 0
                
    
#     for i in range(len(arr)) :
#         for j in range(len(arr[i])) :
#             if arr[i][j] == arr[j][i] :
#                 answer = 1
                
#             elif arr[i][j] != arr[j][i] :
#                 print(arr[i][j], arr[j][i])
#                 answer = 0
                
#             break
#         break
    
    return answer