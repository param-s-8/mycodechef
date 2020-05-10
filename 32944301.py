for _ in range(int(input())):
    p=input().split('#')
    r=0
    t=0
    for i in p:
        if len(i)>t:
            t=len(i)
            r+=1
    print(r)    
        