import os
def reverse(S,start,end):
    if(start>=end):
        return
    S[start],S[end] = S[end],S[start]
    reverse(S,start+1,end-1)
str=['S','H','U','H','A','I','L']
reverse(str,0,len(str)-1)
print(str)


def f(x):
    return x%2!=0 and x%3!=0

result = filter(f,range(1,20))
print(result)

print(os.listdir('/'))

names=['shu','rashi','nooru']
print(names)
print(','.join(names))

my_name='Shuhail'
print(my_name)
print(my_name[::-1])