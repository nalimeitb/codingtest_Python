def solution(arr):
    stack = []
    tmp = None
    
    for i in arr :
        if i != tmp :
            stack.append(i)
            tmp = i
        else :
            continue
    
    
#     tmp = None
    
#     for i in arr :
#         if tmp != i :
#             answer.append(i)
#             tmp = i
#         else :
#             continue
    
    return stack