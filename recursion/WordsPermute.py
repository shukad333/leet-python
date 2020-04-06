def print_str(list):
    print(''.join(list))

def permutation(A,l,r):
    if l==r:
        print_str(A)
    else:
        for i in range(l,r+1):
            A[l],A[i] = A[i],A[l]
            permutation(A,l+1,r)
            A[l], A[i] = A[i], A[l]

A="Shu"
permutation(list(A),0,len(A)-1)
