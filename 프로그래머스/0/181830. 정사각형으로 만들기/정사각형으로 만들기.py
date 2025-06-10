def solution(arr):
    answer = [[]]
    yeol = len(arr)
    hang = len(arr[0])
    
        
    if yeol > hang :
        for i in arr :
            for k in range(yeol - len(i)) :
                i.append(0)
    
    elif hang > yeol :
        for i in range(hang-yeol) :
            arr.append([])
            
        for i in range(yeol,hang) :
            for k in range(hang) :
                arr[i].append(0)
    
    answer = arr
    
    return answer