def solution(picture, k):
    answer = []
    tmp = ''
    
    for i in range(len(picture)) :
        tmp = ''
        for j in range(len(picture[i])) :
            tmp = tmp + picture[i][j] * k
        picture[i] = tmp
    
    for i in range(len(picture)) :
        for j in range(k) :
            answer.append(picture[i])
    
    
    
    return answer