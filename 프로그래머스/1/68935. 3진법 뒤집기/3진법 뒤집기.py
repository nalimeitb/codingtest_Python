def solution(n):
    answer = 0
    
    a = 0
    jb3 = ""
    
    if n < 3 :
        return n
    
    while n // 3 >= 3 :
        jb3 = jb3 + str(n % 3)
        n = n // 3
        
    jb3 = jb3 + str(n%3) + str(n//3)
    
    print(jb3)
    
    for i in range(len(jb3)-1, -1, -1) :
        print(jb3[i], 3**a)
        answer = answer + (int(jb3[i]) * (3**a))
        a = a + 1
        
    
    return answer