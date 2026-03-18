#This uses memory for new string

# def validPalindrome(s):
#     new_str = ""
#     for char in s:
#         if char.isalnum():
#             new_str += char.lower()

#     print(f"string :: {new_str}, new str :: {new_str[::-1]}")
#     return new_str == new_str[::-1]

# s = "A man, a plan, a canal: Panama"
# validPalindrome(s)

def validPalindrome(s):
    l = 0
    r = len(s) - 1
    while l < r:
        while l < r and not alphanum(s[l]):
            l +=1
        while r > l and not alphanum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l+1, r-1
    

def alphanum(c):
    return (ord("A") <= ord(c) <= ord("Z") or
            ord("a") <= ord(c) <= ord("z") or
            ord(0) <= ord(c) <= ord(9)
    )