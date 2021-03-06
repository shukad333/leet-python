"""
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.



Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false


"""

def buddyStrings(A,B):
    if(len(A)!=len(B)): return False
    if A==B and len(set(A)) < len(A):
        return True
    dif = [(a,b) for a,b in zip(A,B) if (a!=b)]
    print(dif[1])
    print(dif[1][::-1])
    return len(dif)==2 and dif[0] == dif[1][::-1]

A="aab"
B="aba"

print(buddyStrings(A,B))