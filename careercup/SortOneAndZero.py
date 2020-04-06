"""

sort zero to left and one to right

"""

class Solution:
    def sortonesandzeros(self,arr):
        zeros,ones=0,len(arr)-1
        while zeros<ones:
            while zeros<ones and arr[zeros]==0:
                zeros+=1
            while zeros<ones and arr[ones]==1:
                ones-=1
            if zeros<len(arr) and ones>=0:
                arr[zeros], arr[ones] = arr[ones], arr[zeros]
                zeros += 1
                ones -= 1



arr = [0,1,1,0,1,1,0,0,1]
sol = Solution()
sol.sortonesandzeros(arr)
print(arr)