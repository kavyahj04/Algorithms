def findClosestSum(nums, target):
    closest = nums[0] + nums[1] + nums[2]
    for i, num in enumerate(nums):
        if i > 0 and nums[i-1] == num:
            continue
        l , r = i + 1, len(nums) - 1
        while l < r:
            sum3 = num + nums[l] + nums[r]
            diff = target - sum3
            if abs(diff) < abs(target - closest):
                closest = sum3
            if sum3 > target :
                r -=1
            elif sum3 < target:
                l += 1
            else:
                print(sum3)
                return sum3
    print(closest)
    return closest

nums = [-1,2,1,-4]
target = 1

findClosestSum(nums, target)