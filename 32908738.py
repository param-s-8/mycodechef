for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    k=int(input())
    key=a[k-1]
    a.sort()
    print(a.index(key)+1)