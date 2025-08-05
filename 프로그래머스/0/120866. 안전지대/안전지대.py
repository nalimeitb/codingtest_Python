def solution(board):
    answer = 0
    list1 = []
    
    if len(board) == 1 :
        if board[0][0] == 1 :
            return 0
        else :
            return 1
    
    for i in range(len(board)) :
        for k in range(len(board)) :
            if board[i][k] != 0 :
                list1.append([i,k])
                
    for i, k in list1 :
        #1
        if 0 < i < len(board)-1 and 0 < k < len(board) - 1 :
            board[i-1][k-1] = 1
            board[i-1][k] = 1
            board[i-1][k+1] = 1
            board[i][k-1] = 1
            board[i][k] = 1
            board[i][k+1] = 1
            board[i+1][k-1] = 1
            board[i+1][k] = 1
            board[i+1][k+1] = 1
        
        #2
        elif i == 0 and 0 < k < len(board) - 1 :
            board[i][k-1] = 1
            board[i][k] = 1
            board[i][k+1] = 1
            board[i+1][k-1] = 1
            board[i+1][k] = 1
            board[i+1][k+1] = 1
        
        #3    
        elif i == len(board)-1 and 0 < k < len(board) - 1 :
            board[i-1][k-1] = 1
            board[i-1][k] = 1
            board[i-1][k+1] = 1
            board[i][k-1] = 1
            board[i][k] = 1
            board[i][k+1] = 1
            
        #4    
        elif i == 0 and k == 0 :
            board[i][k] = 1
            board[i][k+1] = 1
            board[i+1][k] = 1
            board[i+1][k+1] = 1
            
        #5    
        elif 0 < i < len(board)-1 and k == 0 :
            board[i-1][k] = 1
            board[i-1][k+1] = 1
            board[i][k] = 1
            board[i][k+1] = 1
            board[i+1][k] = 1
            board[i+1][k+1] = 1
            
        #6    
        elif i == len(board)-1 and k == 0 :
            board[i-1][k] = 1
            board[i-1][k+1] = 1
            board[i][k] = 1
            board[i][k+1] = 1
            
        #7    
        elif i == 0 and k == len(board) - 1 :
            board[i][k-1] = 1
            board[i][k] = 1
            board[i+1][k-1] = 1
            board[i+1][k] = 1
            
        #8
        elif 0 < i < len(board)-1 and k == len(board) - 1 :
            board[i-1][k-1] = 1
            board[i-1][k] = 1
            board[i][k-1] = 1
            board[i][k] = 1
            board[i+1][k-1] = 1
            board[i+1][k] = 1
            
        #9   
        elif i == len(board)-1 and k == len(board) - 1 :
            board[i-1][k-1] = 1
            board[i-1][k] = 1
            board[i][k-1] = 1
            board[i][k] = 1
            
            
            
            
            
    for i in range(len(board)) :
        for k in range(len(board)) :
            if board[i][k] == 0 :
                answer = answer + 1
        
        
    
    return answer