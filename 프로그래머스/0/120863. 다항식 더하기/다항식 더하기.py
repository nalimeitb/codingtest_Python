def solution(polynomial):
    answer = ''
    polynomial = polynomial.split("+")
    print(polynomial)
    
    list1 = list()
    list2 = list()
    
    for i in polynomial :
        if 'x' in i :
            list1.append(i.strip())
        else :
            list2.append(i.strip())
            
    print(list1, list2)
    
    tmp = 0
    
    for i in list1 :
        if i == 'x' :
            tmp = tmp + 1
        else :
            tmp = tmp + int(i[:-1])
    print(tmp)
    
    tmp1 = 0
    
    for k in list2 :
        tmp1 = tmp1 + int(k)
        
    print(tmp1)
    
    if tmp == 0 :
        if tmp1 != 0 :
            answer = answer + str(tmp1)
    
    if tmp != 0 :
        if tmp1 != 0 :
            answer = str(tmp) + 'x' + ' ' + '+' + ' ' + str(tmp1) 
        else :
            answer = str(tmp) + 'x'
    
    if answer.startswith('1x') :
        answer = answer.lstrip('1')
            
            
        
    
    
#     answer = ''
#     tmp = 0
#     list1 = list()
#     list2 = list()
    
#     polynomial = polynomial.split("+")
    
#     for i in polynomial :
#         i = i.strip()
    
#     for i in polynomial :
#         if 'x' in i :
#             list1.append(i)
#         else :
#             list2.append(i)
            
#     print(list1, list2)
    
    
#     tmp = 0
#     tmp1 = 0
    
#     if len(list1) != 0 :
#         for i in list1 :
#             if i == 'x' :
#                 tmp = tmp + 1
#             else :
#                 tmp1 = i.index('x')
#                 tmp = tmp + int(i[:-1])
#         answer = answer + str(tmp) + 'x'
#     ___________________________________________
#     polynomial = polynomial.split(" ")
#     print(polynomial)
    
#     for i in polynomial :
#         i = i.strip()
#         if i == 'x' :
#             list1.append('x')
#         if 'x' in i :
#             list1.append(i[:-1])
#         elif '+' in i :
#             continue
#         else :
#             list2.append(i)
            
#     print(list1)
#     print(list2)
    
#     if list1 != [] :
#         for k in list1 :
#             if k == 'x' :
#                 tmp = tmp + 1
#             else :
#                 tmp = tmp + int(k)
#         answer = str(tmp) + 'x'
    
    
#     if list2 != [] :
#         tmp = 0
#         for j in list2 :
#             tmp = tmp + int(j)
#         answer = answer + ' ' + '+' + ' ' + str(tmp)
    
#     answer= answer.strip(" ")
    
#     if answer.startswith('+') :
#         answer = answer.lstrip('+')
#     elif answer.startswith('1x') :
#         answer = answer.lstrip('1')
        
#     answer = answer.strip(" ")
    
    return answer