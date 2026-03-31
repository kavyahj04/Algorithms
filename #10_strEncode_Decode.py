
def encode(strList):
    new_str = ""
    for s in strList:
        new_str += str(len(s)) + "#" + s
    print(F"{new_str}")
    return new_str


def decode(s):
    res, i = [], 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        len_s = int(s[i:j])
        res.append(s[j+1: j+1+len_s])
        i = j+1+len_s
    print(res)
    return res

strList = ["This", "Is", "Awesome"]
encoded = encode(strList)
decode(encoded)
