"""
n=int(input())
m=int(input())
# a=[[0]*n]*m
# print(a)
a=[[0]*n for i in range(m)]
print(a)
"""
"""
a=["1","2","3","4","5","6","7"]
L=list(map(int,a))
print(a)
print(L)
"""
"""
a=[1,2,3,4,5,6,7,8,9]
print(a)
L=list(map(lambda x:x*1.6, a))
print(L)
L_1=[]
for i in range(len(L)):
    L_1.append(round(L[i],3))
print(L_1)
"""
"""
L=[1,2,3,4,5,6,7,8,9]
L_new=list(map(lambda x:x**2,L))
print(L_new)
"""
"""
L=[1,2,3,5,5,5,2,3,3,3,6,6,8,9,7,4,1,1,1]
L_1=list(filter(lambda x:x==3, L))
print(L_1)
print(L.count(3))
"""
"""
from functools import reduce
L=[1,2,3,4,5]
L_1=reduce(lambda x,y:x+y,L)
print(L_1)
"""
"""
a=int(input())
L=[]
for i in range(a):
    L.append(list(map(int,input().split())))
print(L)
"""
"""
L=[list(map(int,input().split())) for i in range(int(input()))]
print(L)
"""
"""
L=[[1, 1, 1], [1, 1, 1], [1, 1, 1]]
for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j], end=",")
    print()
for i in L:
    print(i)
"""
"""
L=[[1, 1, 1], [2, 2, 2], [1, 1, 1]]
for i in L:
    for j in i:
        print(j,end=",")
    print()
print(L[1])
"""
"""
L=[[2, 4, 7, 3], [4, 5, 6, 9], [1, 0, 4, 2], [7, 8, 4, 7]]
L_1=[]
for i in range(len(L)):
    L_1.append(sorted(L[i]))
print(L_1)
"""
L = [[2, 4, 7, 3], [4, 5, 6, 9], [1, 0, 4, 2], [7, 8, 4, 7]]
L_1 = []
for i in L:
    for j in i:
        L_1.append(j)
L=sorted(L_1)
print(L)
for i in range(0, len(L), 4):
    e_c = L[i : 4 + i]
    if len(e_c) < 4:
        e_c = e_c + [None for y in range(n - len(e_c))]
    print(list(e_c))
