def solution(l, r):
    answer = []
    
    # i = 0
    # tmp = ''
    
#     while True :
#         i = i + 1
#         tmp = bin(i)
#         print(tmp)
#         tmp = tmp[2:]
#         tmp = tmp.replace('1','5')
#         if int(tmp) < l :
#             continue
#         elif l <= int(tmp) <= r :
#             answer.append(int(tmp))
#         else :
#             break
            
#     if answer == [] :
#         answer = [-1]



    tup = ('1', '2', '3', '4', '6', '7', '8', '9')
    
    for i in range(l, r+1) :
        i = str(i)
        for k in i :
            if k in tup :
                break
        else :
            answer.append(int(i))
            
    if answer == [] :
        answer = [-1]
    
            
    return answer