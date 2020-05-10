for _ in range(int(input())):
    l=list(map(int, input().split(' ')))
    s=sum(l)
    if(s==0):
        print('Beginner')
    elif(s==1):
        print('Junior Developer')
    elif(s==2):
        print('Middle Developer')
    elif(s==3):
        print('Senior Developer')
    elif(s==4):
        print('Hacker')
    else:
        print('Jeff Dean')