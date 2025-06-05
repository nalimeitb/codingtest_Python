# def solution(arr):
#     answer = []
#     stk = []
    
#     i = 0
#     print(arr[-1:])
#     while i < len(arr) :
#         if stk == [] :
#             stk.append(arr[i])
#             i = i + 1
#         elif stk != [] :
#             if stk[-1:] == arr[i] :
#                 stk.pop()
#                 i = i + 1
#             elif stk[-1:] != arr[i] :
#                 stk.append(arr[i])
#                 i = i + 1
    
#     if stk == [] :
#         stk = [-1]
        
#     answer = stk
    
#     return answer

def solution(arr):
    answer = []
    stk = []
    
    i = 0
    print(arr[-1:])
    while i < len(arr) :
        if stk == [] :
            stk.append(arr[i])
            i = i + 1
        elif stk != [] :
            if stk[-1] == arr[i] :
                stk.pop()
                i = i + 1
            elif stk[-1] != arr[i] :
                stk.append(arr[i])
                i = i + 1
    
    if stk == [] :
        stk = [-1]
        
    answer = stk
    
    return answer