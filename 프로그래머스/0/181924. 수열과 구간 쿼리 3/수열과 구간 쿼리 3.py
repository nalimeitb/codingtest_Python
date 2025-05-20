def solution(arr, queries):
    answer = []
    a = 0
    
    for i in range(len(queries)) :
        a = arr[queries[i][0]]
        arr[queries[i][0]] = arr[queries[i][1]]
        arr[queries[i][1]] = a
        
    answer = arr
    
    return answer