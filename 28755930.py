for _ in range(int(input())):
    limak=[]
    bob=[]
    a,b=map(int,input().split(' '))
    for num in range(1,1001):
        if(num%2==0):
            bob.append(num)
        else:
            limak.append(num)
        
        if(sum(limak)>a):
            print("Bob")
            break
        if(sum(bob)>b):
            print("Limak")
            break
            
