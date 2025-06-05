def solution(myString, pat):
    answer = ''
    list1 = list()
    
    for i in range(len(myString)+1) :
        if myString[:i].endswith(pat) :
            list1.append(myString[:i])
    answer = max(list1)
    
    return answer