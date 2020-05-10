for _ in range(int(input())):
    s1=input()
    s2=input()
    mc=0
    for i in range(len(s1)):
        if(s1[i]!='?' and s2[i]!='?'):
            if(s1[i]!=s2[i]):
                mc=mc+1
    mm=0
    for i in range(len(s1)):
        if(s1[i]=='?' or s2[i]=='?'):
            mm=mm+1
            continue
        if(s1[i]!=s2[i]):
            mm=mm+1
    print("{} {}".format(mc,mm))