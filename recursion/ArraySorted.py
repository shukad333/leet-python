def sorted(A):
    if len(A)==1:
        return True
    return A[0] >= A[1] and sorted(A[1:])

A=[6,5,10,2,1]
print(sorted(A))
