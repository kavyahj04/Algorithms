def valid_Anagram(str1, str2):
    if(len(str1) != len(str2)):
        return False
    #create two hashmap
    countStr1, countStr2 = {}, {}

    for i in range(len(str1)):
        countStr1[str1[i]] = 1 + countStr1.get(str1[i] , 0)
        countStr2[str2[i]] = 1 + countStr2.get(str2[i], 0)
    
    for key in countStr1:
        if(countStr1[key] != countStr2.get(key, 0)):
            return False
    print("True")
    return True


str1 = "ababab"
str2 = "bababa"

valid_Anagram(str1, str2)

#TC - O(S + T)
#SC - O(S + T)

#other ways to do this 

#1 using Counter method in python 
#2 sort the string and check if they are equal