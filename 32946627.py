def decimalToBinary(n,k):  
    b=bin(n).replace("0b", "")
    if len(b)<k:
        return ((k-len(b))*'0' + b)
    return b
def binaryToDecimal(n): 
    return int(n,2)
for _ in range(int(input())):
    l=[]
    k,s=input().split(' ')
    k=int(k)
    d={}
    final=''
    for num in range(0,2**k):
        l.append(decimalToBinary(num,k))
    
    for i in range(len(l)):
        ele=l[i]
        l[i]=ele[::-1]
    
    for i in range(len(s)):
        d[binaryToDecimal(l[i])]=s[i]
    
    for i in range(len(d)):
        final+=d[i]
        
    print(final)