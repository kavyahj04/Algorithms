def fourSum(nums, target):
    res = []
    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)):

            if j > i+1 and nums[j] == nums[j-1]:
                continue
            b = nums[j]
            l , r = j+1, len(nums) - 1
            while l < r:
                sum4 = a + b + nums[l] + nums[r]
                if sum4 > target:
                    r -= 1
                elif sum4 < target:
                    l += 1
                else:
                    res.append([a,b, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
    print(res)
    return res


nums = [1,0,-1,0,-2,2]
target = 0
fourSum(nums, target)
        
