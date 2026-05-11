from math import ceil

def kokoEatsBananas(piles, h):
    l,r,res=1,max(piles),max(piles)
    while l <= r:
        mid = (l + r ) // 2
        sol = 0
        for n in piles:
            sol += ceil(n/mid)
        if sol > h:
            l = mid + 1
        else:
            res = min(res, mid)
            r = mid - 1
    print(res)
    return res

piles = [3,6,7,11]
h = 8
kokoEatsBananas(piles, h)