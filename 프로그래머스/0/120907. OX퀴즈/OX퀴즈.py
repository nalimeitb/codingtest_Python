def solution(quiz):
    answer = []
    
    for i in quiz :
        list1 = list()
        list1 = i.split(" ")
        if list1[1] == '+' :
            if int(list1[0]) + int(list1[2]) == int(list1[4]) :
                answer.append("O")
            else :
                answer.append("X")

        elif list1[1] == '-' :
            if int(list1[0]) - int(list1[2]) == int(list1[4]) :
                answer.append("O")
            else :
                answer.append("X")
    
    return answer