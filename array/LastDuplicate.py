arr=[1,2,2,3,3,4,5,6,6,7,8,8,9]
for i in reversed(arr):
    print(i)

for a,b in reversed(list(enumerate(arr))):
    if arr[a]==arr[a-1]:
        print(b,a)
        break

print("done")

