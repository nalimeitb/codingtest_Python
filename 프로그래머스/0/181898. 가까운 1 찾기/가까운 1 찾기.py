def solution(arr, idx):
    answer = 0
    i = 0
    
    
#     while True :
#         if i > idx and arr[i] == 1 :
#             answer = i
#             break
                
#         else :
#             i = i + 1
#             continue
    
    
    while True :
        if i <= idx-1 :
            i = i + 1
            continue
        else :
            if arr[i] == 1:
                answer = i
                break
            
            elif arr[i] == 0 :
                if i == len(arr)-1:
                    answer = -1
                    break
                else :
                    i = i + 1
                    continue
        
    return answer