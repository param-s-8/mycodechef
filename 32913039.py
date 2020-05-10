for _ in range(int(input())):
    n,m=map(int,input().split())
    soi={}
    sof={}
    for __ in range(n):
        c,l=map(int,input().split())
        if l in soi.keys():
            soi[l]+=c 
        else:
            soi[l]=c 
    for __ in range(m):
        c,l=map(int,input().split())
        if l in sof.keys():
            sof[l]+=c 
        else:
            sof[l]=c 
    chakra=0
    for key in soi.keys():
        if soi[key]<sof[key]:
            chakra+=sof[key]-soi[key]
    print(chakra)