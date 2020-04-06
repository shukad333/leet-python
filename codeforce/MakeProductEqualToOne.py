"""



"""

input()
A=map(int,input().split())
p,coins,z=1,0,0
A.sort()
for x in A:
    if x>1:
        coins+=x-1
    elif x<0:
        coins = abs(x)-1
        p*=-1
    elif x==0:
        z+=1

if z==0 and p==-1:
    coins+=2
else:
    coins+=z

print(coins)
