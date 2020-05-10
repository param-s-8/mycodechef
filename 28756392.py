for _ in range(int(input())):
    x=int(input())
    c=0
    while(x%10!=0 and c!=100):
        x=x*2
        c=c+1
    if c==100:
        print(-1)
    else:
        print(c)