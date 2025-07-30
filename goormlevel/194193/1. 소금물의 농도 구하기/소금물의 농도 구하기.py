# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N, M = map(float, input().split())

sogeum = 7 * N / 100
nongdo = sogeum / (N+M) * 100
nongdo = round(nongdo - 0.005, 2)

print (f"{nongdo:.2f}")