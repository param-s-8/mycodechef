for _ in range(int(input())):
    n=int(input())
    pm=[]
    for num in range(0, n+1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                pm.append(num)
    sp=[]

    for i in range(len(pm)-1):
        for j in range(i+1,len(pm)):
            if (pm[i]*pm[j]) < n:
                sp.append(pm[i]*pm[j])
    flag=0
    for num in sp:
        if num*2== n or (n-num in sp):
            print('YES')
            flag=1
            break
    if flag==0:
        print('NO')