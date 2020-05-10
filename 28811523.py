for _ in range(int(input())):
    s=input()
    s_=0
    for char in s:
        if char in ['0','1','2','3','4','5','6','7','8','9']:
            s_=s_+int(char)
    print(s_)