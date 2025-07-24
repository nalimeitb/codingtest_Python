def solution(n):
    answer = []
    
    for i in range(n):
        answer.append([])
        for k in range(n):
            answer[i].append(0)
    
    x = 0
    y = 0
    a = 1
    state = 0

    while a <= n * n:
        if state == 0:
            while y < n and answer[x][y] == 0:
                answer[x][y] = a
                a = a + 1
                y = y + 1
            y = y - 1
            x = x + 1
            state = 1

        elif state == 1:
            while x < n and answer[x][y] == 0:
                answer[x][y] = a
                a = a + 1
                x = x + 1
            x = x - 1
            y = y - 1
            state = 2

        elif state == 2:
            while y >= 0 and answer[x][y] == 0:
                answer[x][y] = a
                a = a + 1
                y = y - 1
            y = y + 1
            x = x - 1
            state = 3

        elif state == 3:
            while x >= 0 and answer[x][y] == 0:
                answer[x][y] = a
                a = a + 1
                x = x - 1
            x = x + 1
            y = y + 1
            state = 0
    
#     마지막 시행착오
#     for i in range(n) :
#         answer.append([])
#         for k in range(n) :
#             answer[i].append(0)
    
#     x = 0
#     y = 0
#     a = 1
    
#     # state1
#     while x < n and y < n :
#         answer[x][y] = a
#         a = a + 1
#         y = y + 1
#     # print(x, y)
    
    
#     # state2
#     y = y - 1
#     x = x + 1
#     while x < n and y < n :
#         answer[x][y] = a
#         a = a + 1
#         x = x + 1
#     # print(x, y)
    
    
#     # state3
#     x = x - 1
#     y = y - 1
#     while x < n and y >= 0 :
#         answer[x][y] = a
#         a = a + 1
#         y = y - 1
#     # print(x, y)
    
#     y = y + 1
#     x = x - 1
    
#     # state4
#     while x >= 1 :
#         answer[x][y] = a
#         a = a + 1
#         x = x - 1
#     # print(x, y)
    
#     list1 = []
#     a = 0
#     k = 1
#     tmp = list()
    
#     for i in range(n) :
#         answer.append([])
#         for k in range(n) :
#             answer[i].append(0)
        
#     for i in range(n**2) :
#         list1.append(i+1)
    
#     answer[a][a:a+n] = list1[a:n]
    
#     for i in range(n-a-1) :
#         answer[a+1+i][a+n-1] = list1[n+i]
    
#     answer[a+n][a+n-1:a-1][::-1] = list1[2*n-a-1:3*n-2*a-2]
    
#     answer[a+n-1:a][a][::-1] = list1[3*n-2*a-1:4*n-3*a-4]

# ___________________________________________________________
        
#     answer[a*k][a*k:n*k] = list1[a*k:n*k]

#     for i in range(a*k+1, n*k) :
#         answer[i][n*k-1] = list1[n*k+i-1]

#     answer[n*k-1][a*k:n*k-1] = list1[2*n*k-1:3*n*k-2][::-1]
    
#     for i in range(n*k-1, a*k, -1) :
#         answer[i][a*k] = list1[3*n*k-i+1]

#     a = a + 1
#     k = k + 1
#     n = n - 1
    
#     answer[a*k][a*k:n*k] = list1[a*k:n*k]

#     for i in range(a*k+1, n*k) :
#         answer[i][n*k-1] = list1[n*k+i-1]

#     answer[n*k-1][a*k:n*k-1] = list1[2*n*k-1:3*n*k-2][::-1]
    
#     for i in range(n*k-1, a*k, -1) :
#         answer[i][a*k] = list1[3*n*k-i+1]

# __________________________________________________________

#     answer[a][a:n] = list1[a:n]

#     for i in range(a+1, n) :
#         answer[i][n-1] = list1[n+i-1]

#     answer[n-1][a:n-1] = list1[2*n-1:3*n-2][::-1]

#     for i in range(n-1, a, -1) :
#         answer[i][a] = list1[3*n-i+1]

#     if n % 2 == 0 :
#         for k in range(int(n/2)) :
#             answer[a][a:n] = list1[a:n]

#             for i in range(a+1, n) :
#                 answer[i][n-1] = list1[n+i-1]

#             answer[n-1][a:n-1] = list1[2*n-1:3*n-2][::-1]

#             for i in range(n-1, a, -1) :
#                 answer[i][a] = list1[3*n-i+1]

#             a = a + 1
#             n = n - 1
            
#     else :
#         for k in range(int(n/2)+1) :
#             answer[a][a:n] = list1[a:n]

#             # print(list1)      
#             # print(answer[1:4][5], list1[n:2*n-1])

#             # answer[a+1:n][n] = list1[n:2*n-1]

#             for i in range(a+1, n) :
#                 answer[i][n-1] = list1[n+i-1]

#             answer[n-1][a:n-1] = list1[2*n-1:3*n-2][::-1]
#             # print(list1, list1[3*n-2:4*n-2]) 
#             # list1[3*n-2:4*n-2] = list1[3*n-2:4*n-2][::-1]
#             # print(list1, list1[3*n-2:4*n-2])    

#             for i in range(n-1, a, -1) :
#                 answer[i][a] = list1[3*n-i+1]

#             a = a + 1
#             n = n - 1
    
#     answer[a][0] ~ answer[a][n]
#     ~
#     answer[a+1][n] ~ answer[n][n]
#     ~
#     answer[n][n-1] ~ answer[n][a]
#     ~
#     answer[n-1][a] ~ answer[a+1][a]
    
    return answer