l=[9,10,11]
l1=[0,0,0,0,0,0,0,0]
for _ in range(int(input())):
    for __ in range(int(input())):
        p,s=map(int,input().split(' '))
        if(p in l):
            continue
        else:
            if(l1[p-1]<s):
                l1[p-1]=s
    print(sum(l1))
    l1=[0]*8
    