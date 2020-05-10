for _ in range(int(input())):
    c=0
    h,m=map(int,input().split(' '))
    for i in range(h):
        for j in range(m):
            li=list(str(i))
            lj=list(str(j))
            if(len(str(i))==2 and len(str(j))==2):
                if(li[0]==li[1]==lj[0]==lj[1]):
                    c=c+1
            elif(len(str(i))==2 and len(str(j))==1):
                if(li[0]==li[1]==lj[0]):
                    c=c+1
            elif(len(str(i))==1 and len(str(j))==2):
                if(li[0]==lj[0]==lj[1]):
                    c=c+1
            else:
                if(li[0]==lj[0]):
                    c=c+1
    print(c)