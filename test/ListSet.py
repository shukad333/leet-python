import collections
import itertools
# list=[1,1,2,3]
# set={1,1,2,3}
# map={"a":"shu"}
# print(list,set,map)
# print(map.get("a"))
print(0^1)

m = collections.defaultdict(list)
print(m)
A=[1,2,3,4]
resp=[-1] * len(A)

#print(resp)

A=[1,2,3,4]
for i in itertools.permutations(A):
    print(i)