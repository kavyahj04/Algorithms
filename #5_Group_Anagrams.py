from collections import defaultdict

def groupAnagrams(strs):
    elements = defaultdict(list)
    for i in range(len(strs)):
        #create [0,0,0......0] for each string 
        count = [0] * 26
        for char in strs[i]:
            #everytime a character appeared add +1,
            count[ord(char) - ord("a")] += 1

        #grouping
        #tuple because list cant be used as key directly
        #instead of assigning directly which overwrites make it appended so it gets group of elements as list

        elements[tuple(count)].append(strs[i])
    print(f"{elements.values()}")
    return elements.values()

strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)