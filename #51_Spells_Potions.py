def successfulPairs(spells, potions, success):

    #Bruteforce

    # p, out = [], []
    # for i in range(len(spells)):
    #     for j in range(len(potions)):
    #         p.append(spells[i] * potions[j])
    #     res = 0
    #     for j in range(len(p)):
    #         if p[j] >= success:
    #             res = res + 1
    #     out.append(res)
    # return out
    potions = sorted(potions)
    out = []
    for i in range(len(spells)):
        left,right = 0, len(potions) - 1
        while left <= right:
            mid = (left + right) // 2
            if((potions[mid] * spells[i]) < success):
                left = mid + 1
            else:
                right = mid - 1
        out.append(len(potions) - left)
    print(out)
    return out

spells = [5,1,3] 
potions = [1,2,3,4,5] 
success = 7
successfulPairs(spells, potions, success)