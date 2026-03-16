def encode(strList):
    res = ""
    for s in strList:
        lengthStr = len(s)
        res += str(lengthStr) + "#" + s
    print(f"The encoded string is :: {res}")
    return res

def decode(str):
    res, i = [], 0
    while i < len(str):
        j = i
        while(str[j] != "#"):
            j += 1
        lengthStr = int(str[i : j])
        res.append(str[j+1 : j+1+lengthStr])
        i = j+1+lengthStr
    print(f"The decoded List is :: {res}")
    return res
    
strList = ["This", "Is", "Awesome"]
encoded = encode(strList)
decode(encoded)