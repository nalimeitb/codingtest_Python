def solution(num_list, n):
    answer = []
    k = 0
    
    for i in range(len(num_list)//n) :
        answer.append(num_list[k*n:(k+1)*n])
        k = k + 1
        
    
    return answer