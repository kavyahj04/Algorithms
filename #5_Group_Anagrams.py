from collections import defaultdict

def groupAnagrams(strs):
    grp = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            index = ord(c) - ord("a")
            count[index] += 1
        
        grp[tuple(count)].append(s)
    print(grp.values())
    return grp.values()


strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)