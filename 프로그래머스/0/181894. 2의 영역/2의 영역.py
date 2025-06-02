def solution(arr):
    answer = []
    list1 = []
        
    if arr.count(2) == 0 :
        answer = [-1]
        
    elif arr.count(2) == 1 :
        answer = [2]
        
    else :
        for i in range(len(arr)) :
            if arr[i] == 2 :
                list1.append(i)
                
        a = list1[:1][0]
        b = list1[-1:][0]
        for k in range(a, b+1,1) :
            answer.append(arr[k])
        
    return answer