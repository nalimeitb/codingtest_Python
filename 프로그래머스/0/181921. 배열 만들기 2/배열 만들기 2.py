def solution(l, r):
    answer = []
    i = 0
    tmp = ''
    
    while True :
        i = i + 1
        tmp = bin(i)
        tmp = tmp[2:]
        tmp = tmp.replace('1','5')
        if int(tmp) < l :
            continue
        elif l <= int(tmp) <= r :
            answer.append(int(tmp))
        else :
            break
            
    if answer == [] :
        answer = [-1]
            
    return answer