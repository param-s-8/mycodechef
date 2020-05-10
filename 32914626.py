for _ in range(int(input())):
    n,m=map(int,input().split(' '))
    total=0
    p=list(map(int,input().split(' ')))
    pl=[]
    for __ in range(n):
        pl.append(list(map(int,input().split(' ')))[1:])
    for i in pl:
        i.sort()
    for i in p:
        total+=pl[i][-1]
        pl[i][-1]=0
        pl[i].sort()
    print(total)    
    