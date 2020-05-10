k,n=map(int,input().split())
kl=[]
for _ in range(k):
    kl.append(input())
for _ in range(n):
    s=input()
    if len(s)>=47:
        print('Good')
    else:
        ans='Bad'
        for i in kl:
            if i in s:
                ans='Good'
                break
        print(ans)