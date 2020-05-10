t=int(input())
l=[]
for _ in range(t):
    a=int(input())
    l.append(a)
for num in l:
    c=0
    for i in str(num):
        if i=='4':
            c=c+1
    print(c)