def solution(i, j, k):
    answer = 0
    str1 = ''
    
    for i in range(i, j+1, 1) :
        str1 = str1 + str(i)
    
    for i in str1 :
        if i == str(k) :
            answer = answer + 1
    
    return answer