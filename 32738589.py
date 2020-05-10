# cook your dish here
for _ in range(int(input())):
    n,q=map(int,input().split(' '))
    s=input()
    for __ in range(q):
        c=int(input())
        alpha=[]
        #pend=[]
        for ltr in s:
            if alpha.count(ltr) < c:
                alpha.append(ltr)
        print(n-len(alpha))
                    