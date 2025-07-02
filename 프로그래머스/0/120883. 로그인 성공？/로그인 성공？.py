def solution(id_pw, db):
    answer = ''
    
    list1 = list()
    for x,y in db :
        list1.append(x)
    
    if id_pw[0] not in list1 :
        answer = 'fail'
    else :
        for x,y in db :
            if x == id_pw[0] and y == id_pw[1] :
                answer = 'login'
                break
            elif y != id_pw[1] :
                answer = 'wrong pw'
        
    
    return answer