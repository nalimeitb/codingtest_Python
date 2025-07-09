def solution(s):
    answer = True

    s = list(s)
    
    for i in range(len(s)) :
        if s[i] == '(' :
            s[i] = 1
        else :
            s[i] = -1
    
    sum1 = list()
    tmp = 0
    
    for i in s :
        tmp = tmp + i
        sum1.append(tmp)
        
    if -1 in sum1 :
        answer = False
        
    if sum1[len(sum1)-1] != 0 :
        answer = False
            
        
    
#     while len(s) != 0 :
#         a = 0

#         if s[0] == '(' :
#             s.pop(0)
#             a = a + 1
#         else :
#             answer = False
#             break

#         while a != 0 :
#             if s[0] == ')' :
#                 a = a - 1
#                 s.pop(0)
                
#             else :
#                 answer = False
#                 break

    

    return answer