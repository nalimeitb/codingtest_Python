def solution(arr, flag):
    answer = []
    
    for i in range(len(arr)) :
        if flag[i] == True :
            for k in range(2 * arr[i]) :
                answer.append(arr[i])
        else :
            for k in range(arr[i]) :
                answer.pop()
    
    return answer