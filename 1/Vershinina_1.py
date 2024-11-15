def func(a,b,c):
    a=int(input())
    if a>0:
        m=0
        if a>m:
            m=a
        if b>m:
            m=b
        if c>m:
            m=c
        return m
    else:
        return -1
s=func(a=0,b=10,c=2)
print(s)
            
