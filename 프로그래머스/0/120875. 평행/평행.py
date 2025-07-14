def solution(dots):
    answer = 0
    list1 = list()
    list2 = list()
    list3 = list()
    
    if (dots[0][1] - dots[1][1])/(dots[0][0] - dots[1][0]) == (dots[2][1] - dots[3][1])/(dots[2][0] - dots[3][0]) :
        answer = 1
    
    if (dots[0][1] - dots[2][1])/(dots[0][0] - dots[2][0]) == (dots[1][1] - dots[3][1])/(dots[1][0] - dots[3][0]) :
        answer = 1
    if (dots[0][1] - dots[3][1])/(dots[0][0] - dots[3][0]) == (dots[1][1] - dots[2][1])/(dots[1][0] - dots[2][0]) :
        answer = 1
    
#     if
    
#     list1.append()
#     list1.append()
#     list1.append()
    
#     list2.append()
#     list2.append((dots[1][1] - dots[3][1])/(dots[1][0] - dots[3][0]))
    
#     list3.append()
    
#     for i in list1 :
#         if i in list2 :
#             answer = 1
#         if i in list3 :
#             answer = 1
            
#     print(list1)
#     print(list2)
#     print(list3)
    
    return answer