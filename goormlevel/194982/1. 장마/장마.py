# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# N, M = map(int, input().split())

# list1 = list(map(int, input().split()))
# list2 = list()
# list3 = list1.copy()
# list2.append(list3[:])

# # print(list2)

# for i in range(M) :
# 	# print(i)
# 	O, P = map(int, input().split())

# 	for k in range(O-1, P) :
# 		list1[k] = list1[k] + 1
# 	# print("list1은 변하는중 : ", list1)	
# 	if i % 3 == 2 :
# 		# print("---------------------------------")
# 		# print("i % 3 == 2 일때의", i)
# 		list3 = list1.copy()
# 		list2.append(list3[:])
# 		# print(list2)
# 		for j in range(N) :
# 			if list2[i//3 + 1][j] != list2[i//3][j] :
# 				# print(list2[i//3 + 1][j], list2[0][j])
# 				list1[j] = list1[j] - 1
# 		# print("배수가 적용된 후 리스트", list1)
# 		# print("---------------------------------")

# answer = ''
# for i in list1 :
# 	answer = answer + str(i) + ' '
# answer = answer.rstrip(" ")
# print(answer)

N, M = map(int, input().split())

list1 = list(map(int, input().split()))
rainspot = [0] * N


for i in range(M) :
	O, P = map(int, input().split())

	for k in range(O-1, P) :
		list1[k] = list1[k] + 1
		rainspot[k] = rainspot[k] + 1
	
	if i % 3 == 2 :
		for j in range(N) :
			if rainspot[j] != 0 :
				list1[j] = list1[j] - 1
		rainspot = [0] * N
			
answer = ''
for i in list1 :
	answer = answer + str(i) + ' '
answer = answer.rstrip(" ")
print(answer)
