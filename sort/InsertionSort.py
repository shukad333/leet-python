"""

Insertion Sort

"""


def insertionSort(arr):

    for i in range(1,len(arr)):
        key = arr[i]

        j = i-1

        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

x=[4,3,7,1,9,0]
print(insertionSort(x))
print(x)