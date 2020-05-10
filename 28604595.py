for _ in range(int(input())):
    d,n=map(int,input().split(' '))
    for d in range(d):
        s=0
        for num in range(1,n+1):
            s=s+num
        n=s
    print(s)