for _ in range(int(input())):
    n=int(input())
    s=str(n)
    l=list(str(n))
    if(l[0]!='0'):
        sr=s[::-1]
        if(s==sr):
            print("wins")
        else:
            print("losses")
    else:
        print("losses")