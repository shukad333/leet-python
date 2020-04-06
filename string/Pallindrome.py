def reverse(s):
    return s[::-1]

def pallindrome(s):
    rev = reverse(s)

    if(s==rev):
        return True
    return False



print(pallindrome("shu"))
print(pallindrome("malayalam"))