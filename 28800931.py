l1=[2,3,9]
for _ in range(int(input())):
    c=0
    l,r=map(int,input().split(' '))
    for num in range(l,r+1):
        if(num%10 in l1):
            c=c+1
    print(c)
        
