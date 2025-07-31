def solution(clothes):
    answer = 1
    dic1 = dict()
    
    for x,y in clothes :
        dic1[y] = dic1.get(y, 0) + 1
        
    # print(dic1)
    
    for i in dic1.values() :
        answer = answer * (i+1)
        
#     cloth face headgear
#     3       2       1
    
#     3 + 2 + 1 = 6
#     3*2 + 3*1 + 2*1 = 11
#     3*2*1 = 6
#     결국에 이건, 각 의상종류에 대해서 선택을 안할지 부터 어떤 의상을 선택할 것인지(개수 + 1)
#     하지만, 모두 다 안입는건 경우에 없으니 마지막에 1 빼주는거
    
    return answer-1