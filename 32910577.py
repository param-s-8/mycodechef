import math
def dist(pt1,pt2):
    return  ((pt2[0]-pt1[0])**2) + ((pt2[1]-pt1[1])**2) 
    
count=0
for _ in range(int(input())):
    l=list(map(int,input().split()))
    pt1=l[0:2]
    pt2=l[2:4]
    pt3=l[4:6]
    s1=dist(pt1,pt2)
    s2=dist(pt2,pt3)
    s3=dist(pt3,pt1)
    if s1+s2==s3 or s2+s3==s1 or s1+s3==s2:
        count+=1

print(count)