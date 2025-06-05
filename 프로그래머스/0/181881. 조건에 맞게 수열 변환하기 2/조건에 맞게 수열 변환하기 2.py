def solution(arr):
    answer = 0
    i = 0
    arr_rep = list()
    arr_rep.append(arr)
    
    
    while True :
        i = i + 1
        arr_rep.append([])
        for k in range(len(arr)) :
            if arr_rep[i-1][k] >= 50 and arr_rep[i-1][k] % 2 == 0 :
                arr_rep[i].append(arr_rep[i-1][k] / 2)
            elif arr_rep[i-1][k] < 50 and arr_rep[i-1][k] % 2 != 0 :
                arr_rep[i].append(arr_rep[i-1][k] * 2 + 1)
            else :
                arr_rep[i].append(arr_rep[i-1][k])
                
        if arr_rep[i] == arr_rep[i-1] :
            answer = i-1
            break
        
        else :
            continue
                

    return answer