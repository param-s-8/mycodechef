d={0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
for _ in range(int(input())):
    a,b=input().split(' ')
    s=int(a)+int(b)
    m=0
    for i in str(s):
        k=d.get(int(i))
        m=m+k
    print(m)
        
