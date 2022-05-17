"""
s="abcde"
i=2
print(s)
print(s[:i])
print(s[i:])
"""
"""
def period(s):
    a=s
    if len(set(s))==1:
        a=str(len(s))+s[0]
    else:
        for t in range(2,len(s)):
            if len(s)%t==0 and s.count(s[:t])==len(s)//t:
                a=str(len(s)//t)+"("+compress(s[:t])+")"
                break
    if len(a)<=len(s):
        s=a
    return s

def compress(s):
    r=s
    for i in range(len(s)):
        if len(period(s[:i])+period(s[i:]))<len(r):
            r=period(s[:i])+period(s[i:])
    return r
        
s=input()
print(compress(s))
"""
"""
#
##
###
####
"""
"""
def blok(L):
    for i in range(len(L)-1,-1,-1):
        if L[i]>0:
            print(L[i]*"#")

L=[4,3,2,1]
blok(L)
"""
def blok(L):
    for i in range(len(L)):
        if L[i]>0:
            print(L[i]*"#")

L=[1,2,3,4]
blok(L)
















