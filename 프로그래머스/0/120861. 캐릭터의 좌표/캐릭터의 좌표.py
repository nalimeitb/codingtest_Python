def solution(keyinput, board):
    
    answer = [0, 0]
    
    #left => x좌표 : -1
    #right => x좌표 : +1
    #up => y좌표 : +1
    #down => y좌표 : -1
    
    for i in keyinput :
        if i == "left" :
            answer[0] = answer[0] - 1
        elif i == "right" :
            answer[0] = answer[0] + 1
        elif i == "up" :
            answer[1] = answer[1] + 1
        elif i == "down" :
            answer[1] = answer[1] - 1
            
        if answer[0] < -((board[0]-1) / 2) :
            answer[0] = -((board[0]-1) / 2)
        elif answer[0] > ((board[0]-1) / 2) :
            answer[0] = ((board[0]-1) / 2)
        if answer[1] < -((board[1]-1) / 2) :
            answer[1] = -((board[1]-1) / 2)
        elif answer[1] > ((board[1]-1) / 2) :
            answer[1] = ((board[1]-1) / 2)
    
    return answer