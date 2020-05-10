for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    count=0
    for i in range(len(l)):
        if i==0:
            if l[i]!=l[i+1]:
                count+=1 
        else:
            if i==len(l)-1:
                if l[i]!=l[i-1]:
                    count+=1
            else:
                if l[i]!=l[i-1] or l[i]!=l[i+1]:
                    count+=1 
    print(count)
        