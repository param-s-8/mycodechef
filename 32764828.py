t,m=input().split(' ')
alpha='abcdefghijklmnopqrstuvwxyz'
d={}
i=0
for ltr in alpha:
    d[ltr]=m[i]
    i+=1
for _ in range(int(t)):
    final=""
    s=input()
    for ltr in s:
        if ltr in ['.',',','?','!']:
            final+=ltr
        elif ltr=='_':
            final+=' '
        else:
            if ltr.isupper():
                final+=d.get(ltr.lower()).upper()
            else:
                final+=d.get(ltr)
    print(final)

    
    