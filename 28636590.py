n=int(input())
l=list(map(int,input().split(' ')))
even=0
odd=0
for num in l:
    if num%2==0:
        even=even+1
    else:
        odd=odd+1
if(even>odd):
    print("READY FOR BATTLE")
else:
    print("NOT READY")