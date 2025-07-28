# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# x, y, z = input().split()
# x = int(x)
# y = int(y)
# z = int(z)

# print ("Hello Goorm! Your input is " , (x + y + z))

k = int(input())

for i in range(k) :
	a, b, c = input().split()
	a = int(a)
	b = int(b)
	c = int(c)
	d = c - abs(a) - abs(b)
	if c == abs(a) + abs(b) :
		print("YES")
	elif d > 0 :
		if d % 2 == 0 :
			print("YES")
		else :
			print("NO")
	else :
		print("NO")