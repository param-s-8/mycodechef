for _ in range(int(input())):
    c=0
    n,k=map(int,input().split(' '))
    l=list(map(int,input().split(' ')))
    for num in l:
        if(sum(l)-num<num+k):
            c=c+1
    print(c)