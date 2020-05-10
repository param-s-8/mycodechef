import math
for i in range(int(input())) :
    a = int(input())
    z = (math.sqrt(1+8*a)-1)//2
    y = z+1
    print(int(min(z + a - z*(z+1)//2 , y + y*(y+1)//2 - a )))