#for given sorted array eg [-4, -3, 2, 3, 4] squae it and sort again [4, 9, 9, 16, 16]

def sqSortedArray(nums):
    res = [0] * len(nums)
    l = 0
    r = len(nums) - 1
    pos = len(nums) - 1
    while l <= r :
        if abs(nums[r]) > abs(nums[l]):
            res[pos] = nums[r] ** 2
            pos -= 1
            r -=1 
        elif abs(nums[l]) > abs(nums[r]):
            res[pos] = nums[l] ** 2
            pos -= 1
            l +=1 
        else:
            res[pos] = nums[l] ** 2
            pos -= 1
            if l != r:
                res[pos] = nums[r] ** 2
                pos-=1
            l += 1
            r -= 1
    print(res)
    return res 

nums = [-4, -3, 2, 3, 4]
sqSortedArray(nums)
