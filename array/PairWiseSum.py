def sumWithPair():
    a = [1, 2, 3, 4, 5, 6]
    map = {}
    sum = 8
    for i in range(0, len(a)):
        print(i)
        if map.get(a[i]) is None:
            map[a[i]] = True
    for i in range(0, len(a)):
        if map.get(sum - a[i]) is not None:
            print("Pair :::", (a[i], sum - a[i]))

def sumPairLogicB(arr,sum):
    """

    :return:
    """
    l=0
    r=len(arr)-1
    while l<=r:
        if arr[l]+arr[r]<sum:
            l+=1
        elif arr[l]+arr[r]>sum:
            r-=1
        else:
            print("Pair",(arr[l],arr[r]))
            l+=1
            r-=1


#sumWithPair()
sumPairLogicB([1,2,3,4,5,6],10)
