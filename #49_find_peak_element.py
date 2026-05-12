def findPeak(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        m = ( l + r ) // 2
        if nums[m] > nums[m + 1 ] and nums[m] < nums[m - 1]:
            print(f("m: " + {m}))
            return m
        elif nums[m] < nums[m+1]:
            l = m + 1
        else:
            r = m
    print(l)
    return l

nums = [1,2,1,3,5,6,4]
findPeak(nums)