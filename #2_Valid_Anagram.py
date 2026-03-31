
#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def valid_Anagram(str1, str2):
    if len(str1) != len(str2):
        print("False")
        return False 
    
    s1 = {}
    s2 = {}

    for i in range(len(str1)):
        s1[str1[i]] = 1 + s1.get(str1[i], 0)
        s2[str2[i]] = 1 + s2.get(str2[i], 0)
    
    for key in s1:
        if s1[key] != s2[key]:
            print("False")
            return False
    print("True")
    return True

str1 = "anagram"
str2 = "nagaarmkj"
valid_Anagram(str1, str2)
#TC - O(S + T)
#SC - O(S + T)

#other ways to do this 

#1 using Counter method in python 
#2 sort the string and check if they are equal