def solution(l, r):
    answer = []
    val = ''
    i = 0
    
    while True :
        i = i + 1
        val = bin(i)
        val = val[2:]
        val = val.replace('1', '5')
        val = int(val)
        if val < l :
            continue
        elif l <= val <= r :
            answer.append(val)
        elif val > r :
            break
            
    if answer == [] :
        answer = [-1]
    
    
    return answer