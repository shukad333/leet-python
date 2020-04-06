class BubbleSort:
    def __init__(self,arr):
        self.arr = arr

    def sort(self):
        arr = self.arr

        for i in range(len(arr)):
            for j in range(0,len(arr)-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [4,3,5,1,8,6,9,0]
b = BubbleSort(arr)
b.sort()
print(arr)
