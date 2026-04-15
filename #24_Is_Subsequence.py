#check if s is subsequence of y
def isSubSequence(s, t):
    i, j = 0, 0
    while i< len(s) and  j < len(t):
        if s[i] == t[j]:
            i+=1
        j+=1
    print(i == len(s))
    return i == len(s)

    
s = "abc"
t = "ahbgdc"
isSubSequence(s, t)