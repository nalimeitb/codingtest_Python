def solution(M, N):
    answer = 0
    
    if M <= N :
        answer = (M-1) + M * (N-1)
    
    else :
        answer = (N-1) + (M-1) * N
    
    if M == 1 and N == 1 :
        answer = 0
    
    return answer