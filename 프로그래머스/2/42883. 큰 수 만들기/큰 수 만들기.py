def solution(number, k):
    answer = ''
    
#     stack을 활용한 풀이
    stack = []
    
    for i in number :
        while stack and k > 0 and stack[-1] < i :
            stack.pop()
            k = k - 1
        stack.append(i)
        
    answer = ''.join(stack[:len(number)-k])
    
#     시간복잡도 높아서 효율성 나쁨..
#     number = list(number)
#     j = len(number) - k
    
#     print(number)
    
#     while len(answer) < j :
#         a = 0
#         이부분-> n-k*k 정도 복잡도를 가짐
#         if k < len(number):
#             a = number.index(max(number[0:k+1]))
#         else:
#             a = number.index(max(number))

#         answer = answer + number[a]
        
#         if a != 0 :
#             for i in range(a+1):
#                 number.pop(0)
#         else :
#             number.pop(0)

#         k = k - a
        
#         if k < len(number)-1 :
#             a = number.index(max(number[0:k]))
#         else :
#             a = number.index(max(number))

#         answer = answer + number[a]
        
#         a = a + 1
        
#         for i in range(a) :
#             number.pop(0)
            
#         k = k - a
        
        # if a == 0 :
        #     number.pop(0)
        #     k = k - 1
        # else :
        #     while a != 0 :
        #         number.pop(0)
        #         a = a - 1

#     try :
#         b = number.index(max(number[k:k+k-a]))
#     except :
#         b = number.index(max(number[k:]))
    
#     print(b)
    
    return answer