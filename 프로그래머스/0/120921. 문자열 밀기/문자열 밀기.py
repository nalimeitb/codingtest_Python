def solution(A, B):
    answer = 0
    i = 0
    str1 = ''
    list1 = list()
    
    while str1 not in list1 :
        list1.append(str1)
        str1 = ''
        str1 = A[-i:] + A[:-i]
        i = i + 1
    
    if B in list1 :
        for i in range(len(list1)) :
            if list1[i] == B :
                answer = i-1
    else :
        answer = -1
    return answer