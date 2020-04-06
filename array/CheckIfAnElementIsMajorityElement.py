"""

Check if the given value is a majority element in an array

"""


def isMajority(arr,x):
    def _binarySearch(arr,low,high,x):
        if high>=low:
            mid = (high+low)>>1

            if mid==0 or (x>arr[mid-1] and arr[mid]==x):
                return mid
            elif x>arr[mid]:
                return _binarySearch(arr,mid+1,high,x)
            else:
                return _binarySearch(arr,low,mid-1,x)
        return -1

    i=_binarySearch(arr,0,len(arr)-1,x)
    if i==-1:
        return False
    n=len(arr)
    if i+n//2<n-1 and arr[i+n//2]==x:
        return True
    else:
        return False

arr = [1, 2, 3, 3, 3, 3, 10]
print(isMajority(arr,10))