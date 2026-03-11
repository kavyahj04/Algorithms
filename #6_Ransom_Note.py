#Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

def canConstruct(ransomNote, magazine):
    r_map, m_map = {}, {}

    for i in range(len(ransomNote)):
        r_map[ransomNote[i]] = 1 + r_map.get(ransomNote[i], 0)

    for i in range(len(magazine)):
        m_map[magazine[i]] = 1 + m_map.get(magazine[i], 0)
    
    for i in range(len(ransomNote)):
        if r_map[ransomNote[i]] > m_map.get(ransomNote[i], 0):
            print("False")
            return False
    print("True")
    return True

ransomNote = "a"
magazine = "b"

ransomNote = "aa"
magazine = "ab"

ransomNote = "aa"
magazine = "aab"
canConstruct(ransomNote, magazine)
